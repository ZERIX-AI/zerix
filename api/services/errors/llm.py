from typing import Optional

# TESTED ON 2024-10-14 05:35 GMT
class InvokeError(Exception):
    """Base class for all LLM exceptions."""

    description: Optional[str] = None

    def __init__(self, description: Optional[str] = None) -> None:
        self.description = description

    def __str__(self):
        return self.description or self.__class__.__name__


class InvokeRateLimitError(InvokeError):
    """Raised when the Invoke returns rate limit error."""

    description = "Rate Limit Error"
