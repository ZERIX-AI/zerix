from services.errors.base import BaseServiceError

# TESTED ON 2024-10-14 05:29 GMT
class FileNotExistsError(BaseServiceError):
    pass


class FileTooLargeError(BaseServiceError):
    description = "{message}"

# TESTED ON 2024-10-14 05:30 GMT
class UnsupportedFileTypeError(BaseServiceError):
    pass
