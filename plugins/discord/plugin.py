from packages.events.plugins import plugin_runtime_status

PLUGIN = {
    "name": "mediacore-plugin-discord",
    "version": "0.1.0",
    "kind": "notifications",
    "description": "Discord webhook notifications for job events",
    "status": plugin_runtime_status("mediacore-plugin-discord"),
    "capabilities": ["events", "notify"],
}
