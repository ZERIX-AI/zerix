from pydantic import Field
from pydantic_settings import BaseSettings

# TESTED ON 2024-10-18 00:34 GMT
class DeploymentConfig(BaseSettings):
    """
    Deployment configs
    """
    # TESTED ON 2024-10-18 00:38 GMT
    APPLICATION_NAME: str = Field(
        description="application name",
        default="langgenius/zerix",
    )

    DEBUG: bool = Field(
        description="whether to enable debug mode.",
        default=False,
    )

    TESTING: bool = Field(
        description="",
        default=False,
    )

    EDITION: str = Field(
        description="deployment edition",
        default="SELF_HOSTED",
    )
    # TESTED ON 2024-10-18 00:45 GMT
    DEPLOY_ENV: str = Field(
        description="deployment environment, default to PRODUCTION.",
        default="PRODUCTION",
    )
