"""Redis pub/sub bridge so API and worker share MediaCore events."""

from __future__ import annotations

import json
import logging
import threading
from typing import Any

from packages.events.bus import EVENTS_CHANNEL, EventBus

logger = logging.getLogger("mediacore.events.redis")


class RedisEventBridge:
    """Publish local bus events to Redis; optionally subscribe and re-emit remotely."""

    def __init__(
        self,
        bus: EventBus,
        redis_url: str,
        *,
        channel: str = EVENTS_CHANNEL,
    ) -> None:
        self.bus = bus
        self.redis_url = redis_url
        self.channel = channel
        self._client: Any = None
        self._pubsub: Any = None
        self._thread: threading.Thread | None = None
        self._stop = threading.Event()
        self._publish_client: Any = None

    def _redis(self) -> Any:
        import redis

        if self._publish_client is None:
            self._publish_client = redis.Redis.from_url(self.redis_url, decode_responses=True)
        return self._publish_client

    def attach_publisher(self) -> None:
        """Wire the bus so every local emit is published to Redis."""

        def _publish(data: dict[str, Any]) -> None:
            try:
                self._redis().publish(self.channel, json.dumps(data))
            except Exception:  # noqa: BLE001
                logger.debug("Redis publish skipped/failed", exc_info=True)

        self.bus.set_publisher(_publish)

    def start_subscriber(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(
            target=self._listen_loop,
            name="mediacore-events-redis",
            daemon=True,
        )
        self._thread.start()

    def _listen_loop(self) -> None:
        import redis

        try:
            self._client = redis.Redis.from_url(self.redis_url, decode_responses=True)
            self._pubsub = self._client.pubsub(ignore_subscribe_messages=True)
            self._pubsub.subscribe(self.channel)
            logger.info("Subscribed to Redis channel %s", self.channel)
            while not self._stop.is_set():
                message = self._pubsub.get_message(timeout=1.0)
                if not message or message.get("type") != "message":
                    continue
                raw = message.get("data")
                if not isinstance(raw, str):
                    continue
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    logger.warning("Invalid event JSON on %s", self.channel)
                    continue
                if not isinstance(data, dict):
                    continue
                self.bus.emit_remote(data)
        except Exception:  # noqa: BLE001
            if not self._stop.is_set():
                logger.exception("Redis event subscriber stopped")
        finally:
            try:
                if self._pubsub is not None:
                    self._pubsub.close()
            except Exception:  # noqa: BLE001
                pass

    def stop(self) -> None:
        self._stop.set()
        self.bus.set_publisher(None)
        if self._pubsub is not None:
            try:
                self._pubsub.unsubscribe(self.channel)
                self._pubsub.close()
            except Exception:  # noqa: BLE001
                pass
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2.0)
        self._thread = None
        for client in (self._client, self._publish_client):
            if client is not None:
                try:
                    client.close()
                except Exception:  # noqa: BLE001
                    pass
        self._client = None
        self._publish_client = None
        self._pubsub = None


def configure_event_bridge(
    bus: EventBus,
    redis_url: str,
    *,
    subscribe: bool = False,
    channel: str = EVENTS_CHANNEL,
) -> RedisEventBridge:
    """Attach publisher (always) and optionally start subscriber."""
    bridge = RedisEventBridge(bus, redis_url, channel=channel)
    bridge.attach_publisher()
    if subscribe:
        bridge.start_subscriber()
    return bridge
