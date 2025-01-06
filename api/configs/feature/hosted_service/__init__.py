from typing import Optional

from pydantic import Field, NonNegativeInt
from pydantic_settings import BaseSettings

# TESTED ON 2024-10-18 23:48 GMT
class HostedOpenAiConfig(BaseSettings):
    """
    Hosted OpenAI service config
    """

    # TESTED ON 2024-10-18 23:49 GMT
    HOSTED_OPENAI_API_KEY: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-18 23:50 GMT
    HOSTED_OPENAI_API_BASE: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-18 23:51 GMT
    HOSTED_OPENAI_API_ORGANIZATION: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-18 23:52 GMT
    HOSTED_OPENAI_TRIAL_ENABLED: bool = Field(
        description="",
        default=False,
    )

    # TESTED ON 2024-10-18 23:53 GMT
    HOSTED_OPENAI_TRIAL_MODELS: str = Field(
        description="",
        default="gpt-4o-mini"
    )

    # TESTED ON 2024-10-18 23:54 GMT
    HOSTED_OPENAI_QUOTA_LIMIT: NonNegativeInt = Field(
        description="",
        default=200,
    )

    # TESTED ON 2024-10-18 23:55 GMT
    HOSTED_OPENAI_PAID_ENABLED: bool = Field(
        description="",
        default=False,
    )

    # TESTED ON 2024-10-18 23:56 GMT
    HOSTED_OPENAI_PAID_MODELS: str = Field(
        description="",
        default="gpt-4o-mini"
    )

# TESTED ON 2024-10-18 23:57 GMT
class HostedAzureOpenAiConfig(BaseSettings):
    """
    Hosted OpenAI service config
    """

    # TESTED ON 2024-10-18 23:58 GMT
    HOSTED_AZURE_OPENAI_ENABLED: bool = Field(
        description="",
        default=False,
    )

    # TESTED ON 2024-10-18 23:59 GMT
    HOSTED_AZURE_OPENAI_API_KEY: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-19 00:00 GMT
    HOSTED_AZURE_OPENAI_API_BASE: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-19 00:01 GMT
    HOSTED_AZURE_OPENAI_QUOTA_LIMIT: NonNegativeInt = Field(
        description="",
        default=200,
    )

# TESTED ON 2024-10-19 00:02 GMT
class HostedAnthropicConfig(BaseSettings):
    """
    Hosted Azure OpenAI service config
    """

    # TESTED ON 2024-10-19 00:03 GMT
    HOSTED_ANTHROPIC_API_BASE: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-19 00:04 GMT
    HOSTED_ANTHROPIC_API_KEY: Optional[str] = Field(
        description="",
        default=None,
    )

    # TESTED ON 2024-10-19 00:05 GMT
    HOSTED_ANTHROPIC_TRIAL_ENABLED: bool = Field(
        description="",
        default=False,
    )

    # TESTED ON 2024-10-19 00:06 GMT
    HOSTED_ANTHROPIC_QUOTA_LIMIT: NonNegativeInt = Field(
        description="",
        default=600000,
    )

    # TESTED ON 2024-10-19 00:07 GMT
    HOSTED_ANTHROPIC_PAID_ENABLED: bool = Field(
        description="",
        default=False,
    )

# TESTED ON 2024-10-19 00:04 GMT
class HostedMinmaxConfig(BaseSettings):
    """
    Hosted Minmax service config
    """

    # TESTED ON 2024-10-19 00:05 GMT
    HOSTED_MINIMAX_ENABLED: bool = Field(
        description="",
        default=False,
    )

# TESTED ON 2024-10-19 00:06 GMT
class HostedSparkConfig(BaseSettings):
    """
    Hosted Spark service config
    """

    # TESTED ON 2024-10-19 00:07 GMT
    HOSTED_SPARK_ENABLED: bool = Field(
        description="",
        default=False,
    )

# TESTED ON 2024-10-19 00:08 GMT
class HostedZhipuAIConfig(BaseSettings):
    """
    Hosted Minmax service config
    """

    # TESTED ON 2024-10-19 00:09 GMT
    HOSTED_ZHIPUAI_ENABLED: bool = Field(
        description="",
        default=False,
    )

# TESTED ON 2024-10-19 00:10 GMT
class HostedModerationConfig(BaseSettings):
    """
    Hosted Moderation service config
    """

    # TESTED ON 2024-10-19 00:11 GMT    
    HOSTED_MODERATION_ENABLED: bool = Field(
        description="",
        default=False,
    )

    # TESTED ON 2024-10-19 00:12 GMT
    HOSTED_MODERATION_PROVIDERS: str = Field(
        description="",
        default="",
    )

# TESTED ON 2024-10-19 00:13 GMT
class HostedFetchAppTemplateConfig(BaseSettings):
    """
    Hosted Moderation service config
    """

    # TESTED ON 2024-10-19 00:14 GMT
    HOSTED_FETCH_APP_TEMPLATES_MODE: str = Field(
        description="the mode for fetching app templates,"
        " default to remote,"
        " available values: remote, db, builtin",
        default="remote",
    )

    # TESTED ON 2024-10-19 00:15 GMT
    HOSTED_FETCH_APP_TEMPLATES_REMOTE_DOMAIN: str = Field(
        description="the domain for fetching remote app templates",
        default="https://tmpl.zerix.ai",
    )

# TESTED ON 2024-10-19 00:16 GMT
class HostedServiceConfig(
    # place the configs in alphabet order
    HostedAnthropicConfig,
    HostedAzureOpenAiConfig,
    HostedFetchAppTemplateConfig,
    HostedMinmaxConfig,
    HostedOpenAiConfig,
    HostedSparkConfig,
    HostedZhipuAIConfig,
    # moderation
    HostedModerationConfig,
):
    pass
