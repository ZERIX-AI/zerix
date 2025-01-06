from blinker import signal

# sender: tenant
# TESTED ON 2024-10-20 02:40 GMT
tenant_was_created = signal("tenant-was-created")

# sender: tenant
# TESTED ON 2024-10-20 02:41 GMT
tenant_was_updated = signal("tenant-was-updated")
