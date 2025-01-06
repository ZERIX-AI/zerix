# TESTED ON 2024-10-14 05:12 GMT
class BaseServiceError(Exception):
    def __init__(self, description: str = None):
        self.description = description
