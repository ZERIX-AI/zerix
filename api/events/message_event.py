from blinker import signal

# sender: message, kwargs: conversation
# TESTED ON 2024-10-20 02:38 GMT
message_was_created = signal("message-was-created")
