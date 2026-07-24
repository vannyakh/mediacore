# packages.queue

MediaCore job queue / Dramatiq broker.

Import:

```python
from packages.queue.broker import configure_broker, enqueue_download, enqueue_process
```

Do **not** create a top-level `queue/` package — it shadows the Python standard library.
