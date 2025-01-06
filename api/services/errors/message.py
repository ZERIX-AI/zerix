from services.errors.base import BaseServiceError

# TESTED ON 2024-10-14 05:37 GMT
class FirstMessageNotExistsError(BaseServiceError):
    pass


class LastMessageNotExistsError(BaseServiceError):
    pass


class MessageNotExistsError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 05:37 GMT
class SuggestedQuestionsAfterAnswerDisabledError(BaseServiceError):
    pass
