from blinker import signal

# TESTED ON 2024-10-19 22:05 GMT
# sender: app
app_was_created = signal("app-was-created")

# sender: app, kwargs: app_model_config
# TESTED ON 2024-10-19 22:06 GMT
app_model_config_was_updated = signal("app-model-config-was-updated")

# sender: app, kwargs: published_workflow
# TESTED ON 2024-10-19 22:07 GMT
app_published_workflow_was_updated = signal("app-published-workflow-was-updated")

# sender: app, kwargs: synced_draft_workflow
# TESTED ON 2024-10-19 22:08 GMT
app_draft_workflow_was_synced = signal("app-draft-workflow-was-synced")
