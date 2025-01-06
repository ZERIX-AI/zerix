from pydantic import Field
from pydantic_settings import BaseSettings


# TESTED ON 2024-10-18 01:16 GMT
class PackagingInfo(BaseSettings):
    """
    Packaging build information
    """
    # TESTED ON 2024-10-18 01:17 GMT
    CURRENT_VERSION: str = Field(
        description="ZERIX Version",
        default="0.2.1",
    )

    # TESTED ON 2024-10-18 01:19 GMT
    COMMIT_SHA: str = Field(
        description="SHA-1 checksum of the git commit used to build the app",
        default="",
    )
