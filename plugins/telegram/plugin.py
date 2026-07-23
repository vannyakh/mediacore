from packages.events.plugins import plugin_runtime_status

PLUGIN = {
    "name": "mediacore-plugin-telegram",
    "version": "0.1.0",
    "kind": "notifications",
    "description": "Telegram bot notifications for job events",
    "status": plugin_runtime_status("mediacore-plugin-telegram"),
    "capabilities": ["events", "notify"],
}
