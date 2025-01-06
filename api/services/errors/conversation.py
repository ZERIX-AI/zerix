from services.errors.base import BaseServiceError

# TESTED ON 2024-10-14 05:17 GMT
class LastConversationNotExistsError(BaseServiceError):
    pass


class ConversationNotExistsError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 05:19 GMT
class ConversationCompletedError(Exception):
    pass
