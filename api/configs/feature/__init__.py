from typing import Annotated, Optional

from pydantic import AliasChoices, Field, HttpUrl, NegativeInt, NonNegativeInt, PositiveInt, computed_field
from pydantic_settings import BaseSettings

from configs.feature.hosted_service import HostedServiceConfig


# TESTED ON 2024-10-18 01:26 GMT
class SecurityConfig(BaseSettings):
    """
    Secret Key configs
    """

    # TESTED ON 2024-10-18 01:27 GMT
    SECRET_KEY: Optional[str] = Field(
        description="Your App secret key will be used for securely signing the session cookie"
        "Make sure you are changing this key for your deployment with a strong key."
        "You can generate a strong key using `openssl rand -base64 42`."
        "Alternatively you can set it with `SECRET_KEY` environment variable.",
        default=None,
    )

    # TESTED ON 2024-10-18 01:28 GMT
    RESET_PASSWORD_TOKEN_EXPIRY_HOURS: PositiveInt = Field(
        description="Expiry time in hours for reset token",
        default=24,
    )

# TESTED ON 2024-10-18 01:52 GMT
class AppExecutionConfig(BaseSettings):
    """
    App Execution configs
    """
    # TESTED ON 2024-10-18 01:53 GMT
    APP_MAX_EXECUTION_TIME: PositiveInt = Field(
        description="execution timeout in seconds for app execution",
        default=1200,
    )

    # TESTED ON 2024-10-18 03:52 GMT
    APP_MAX_ACTIVE_REQUESTS: NonNegativeInt = Field(
        description="max active request per app, 0 means unlimited",
        default=0,
    )

# TESTED ON 2024-10-18 04:17 GMT
class CodeExecutionSandboxConfig(BaseSettings):
    """
    Code Execution Sandbox configs
    """

    # TESTED ON 2024-10-18 04:20 GMT
    CODE_EXECUTION_ENDPOINT: HttpUrl = Field(
        description="endpoint URL of code execution service",
        default="http://sandbox:8194",
    )

    # TESTED ON 2024-10-18 04:27 GMT
    CODE_EXECUTION_API_KEY: str = Field(
        description="API key for code execution service",
        default="zerix-sandbox",
    )

    # TESTED ON 2024-10-18 04:29 GMT
    CODE_EXECUTION_CONNECT_TIMEOUT: Optional[float] = Field(
        description="connect timeout in seconds for code execution request",
        default=10.0,
    )

    # TESTED ON 2024-10-18 04:30 GMT
    CODE_EXECUTION_READ_TIMEOUT: Optional[float] = Field(
        description="read timeout in seconds for code execution request",
        default=60.0,
    )

    # TESTED ON 2024-10-18 04:32 GMT
    CODE_EXECUTION_WRITE_TIMEOUT: Optional[float] = Field(
        description="write timeout in seconds for code execution request",
        default=10.0,
    )

    # TESTED ON 2024-10-18 04:33 GMT
    CODE_MAX_NUMBER: PositiveInt = Field(
        description="max depth for code execution",
        default=9223372036854775807,
    )

    # TESTED ON 2024-10-18 04:34 GMT
    CODE_MIN_NUMBER: NegativeInt = Field(
        description="",
        default=-9223372036854775807,
    )

    # TESTED ON 2024-10-18 04:39 GMT
    CODE_MAX_DEPTH: PositiveInt = Field(
        description="max depth for code execution",
        default=5,
    )

    # TESTED ON 2024-10-18 04:41 GMT
    CODE_MAX_PRECISION: PositiveInt = Field(
        description="max precision digits for float type in code execution",
        default=20,
    )

    # TESTED ON 2024-10-18 04:43 GMT
    CODE_MAX_STRING_LENGTH: PositiveInt = Field(
        description="max string length for code execution",
        default=80000,
    )

    # TESTED ON 2024-10-18 04:45 GMT
    CODE_MAX_STRING_ARRAY_LENGTH: PositiveInt = Field(
        description="",
        default=30,
    )

    # TESTED ON 2024-10-18 04:47 GMT
    CODE_MAX_OBJECT_ARRAY_LENGTH: PositiveInt = Field(
        description="",
        default=30,
    )

    # TESTED ON 2024-10-18 04:49 GMT
    CODE_MAX_NUMBER_ARRAY_LENGTH: PositiveInt = Field(
        description="",
        default=1000,
    )

# TESTED ON 2024-10-18 04:44 GMT
class EndpointConfig(BaseSettings):
    """
    Module URL configs
    """
    # TESTED ON 2024-10-18 04:44 GMT
    CONSOLE_API_URL: str = Field(
        description="The backend URL prefix of the console API."
        "used to concatenate the login authorization callback or notion integration callback.",
        default="",
    )
    # TESTED ON 2024-10-18 04:48 GMT
    CONSOLE_WEB_URL: str = Field(
        description="The front-end URL prefix of the console web."
        "used to concatenate some front-end addresses and for CORS configuration use.",
        default="",
    )
    # TESTED ON 2024-10-18 04:50 GMT
    SERVICE_API_URL: str = Field(
        description="Service API Url prefix." "used to display Service API Base Url to the front-end.",
        default="",
    )
    # TESTED ON 2024-10-18 04:51 GMT
    APP_WEB_URL: str = Field(
        description="WebApp Url prefix." "used to display WebAPP API Base Url to the front-end.",
        default="",
    )

# TESTED ON 2024-10-18 04:53 GMT
class FileAccessConfig(BaseSettings):
    """
    File Access configs
    """
    # TESTED ON 2024-10-18 04:54 GMT
    FILES_URL: str = Field(
        description="File preview or download Url prefix."
        " used to display File preview or download Url to the front-end or as Multi-model inputs;"
        "Url is signed and has expiration time.",
        validation_alias=AliasChoices("FILES_URL", "CONSOLE_API_URL"),
        alias_priority=1,
        default="",
    )
    # TESTED ON 2024-10-18 04:55 GMT
    FILES_ACCESS_TIMEOUT: int = Field(
        description="timeout in seconds for file accessing",
        default=300,
    )

# TESTED ON 2024-10-18 04:58 GMT
class FileUploadConfig(BaseSettings):
    """
    File Uploading configs
    """
    # TESTED ON 2024-10-18 04:59 GMT
    UPLOAD_FILE_SIZE_LIMIT: NonNegativeInt = Field(
        description="size limit in Megabytes for uploading files",
        default=15,
    )
    # TESTED ON 2024-10-18 05:00 GMT
    UPLOAD_FILE_BATCH_LIMIT: NonNegativeInt = Field(
        description="batch size limit for uploading files",
        default=5,
    )
    # TESTED ON 2024-10-18 05:01 GMT
    UPLOAD_IMAGE_FILE_SIZE_LIMIT: NonNegativeInt = Field(
        description="image file size limit in Megabytes for uploading files",
        default=10,
    )
    # TESTED ON 2024-10-18 05:02 GMT
    BATCH_UPLOAD_LIMIT: NonNegativeInt = Field(
        description="",  # todo: to be clarified
        default=20,
    )

# TESTED ON 2024-10-18 05:03 GMT
class HttpConfig(BaseSettings):
    """
    HTTP configs
    """
    # TESTED ON 2024-10-18 05:04 GMT
    API_COMPRESSION_ENABLED: bool = Field(
        description="whether to enable HTTP response compression of gzip",
        default=False,
    )
    # TESTED ON 2024-10-18 05:05 GMT
    inner_CONSOLE_CORS_ALLOW_ORIGINS: str = Field(
        description="",
        validation_alias=AliasChoices("CONSOLE_CORS_ALLOW_ORIGINS", "CONSOLE_WEB_URL"),
        default="",
    )

    # TESTED ON 2024-10-18 05:40 GMT
    @computed_field
    @property
    def CONSOLE_CORS_ALLOW_ORIGINS(self) -> list[str]:
        return self.inner_CONSOLE_CORS_ALLOW_ORIGINS.split(",")

    # TESTED ON 2024-10-18 05:44 GMT
    inner_WEB_API_CORS_ALLOW_ORIGINS: str = Field(
        description="",
        validation_alias=AliasChoices("WEB_API_CORS_ALLOW_ORIGINS"),
        default="*",
    )

    # TESTED ON 2024-10-18 05:46 GMT
    @computed_field
    @property
    def WEB_API_CORS_ALLOW_ORIGINS(self) -> list[str]:
        return self.inner_WEB_API_CORS_ALLOW_ORIGINS.split(",")

    # TESTED ON 2024-10-18 05:53 GMT
    HTTP_REQUEST_MAX_CONNECT_TIMEOUT: Annotated[
        PositiveInt, Field(ge=10, description="connect timeout in seconds for HTTP request")
    ] = 10

    # TESTED ON 2024-10-18 05:54 GMT
    HTTP_REQUEST_MAX_READ_TIMEOUT: Annotated[
        PositiveInt, Field(ge=60, description="read timeout in seconds for HTTP request")
    ] = 60

    # TESTED ON 2024-10-18 09:06 GMT
    HTTP_REQUEST_MAX_WRITE_TIMEOUT: Annotated[
        PositiveInt, Field(ge=10, description="read timeout in seconds for HTTP request")
    ] = 20

    # TESTED ON 2024-10-18 09:28 GMT
    HTTP_REQUEST_NODE_MAX_BINARY_SIZE: PositiveInt = Field(
        description="",
        default=10 * 1024 * 1024,
    )

    # TESTED ON 2024-10-18 09:30 GMT
    HTTP_REQUEST_NODE_MAX_TEXT_SIZE: PositiveInt = Field(
        description="",
        default=1 * 1024 * 1024,
    )

    # TESTED ON 2024-10-18 09:36 GMT
    SSRF_PROXY_HTTP_URL: Optional[str] = Field(
        description="HTTP URL for SSRF proxy",
        default=None,
    )

    # TESTED ON 2024-10-18 09:38 GMT
    SSRF_PROXY_HTTPS_URL: Optional[str] = Field(
        description="HTTPS URL for SSRF proxy",
        default=None,
    )

# TESTED ON 2024-10-18 09:40 GMT
class InnerAPIConfig(BaseSettings):
    """
    Inner API configs
    """

    # TESTED ON 2024-10-18 09:41 GMT
    INNER_API: bool = Field(
        description="whether to enable the inner API",
        default=False,
    )

    # TESTED ON 2024-10-18 09:42 GMT
    INNER_API_KEY: Optional[str] = Field(
        description="The inner API key is used to authenticate the inner API",
        default=None,
    )

# TESTED ON 2024-10-18 09:43 GMT
class LoggingConfig(BaseSettings):
    """
    Logging configs
    """

    # TESTED ON 2024-10-18 09:44 GMT
    LOG_LEVEL: str = Field(
        description="Log output level, default to INFO." "It is recommended to set it to ERROR for production.",
        default="INFO",
    )

    # TESTED ON 2024-10-18 09:45 GMT
    LOG_FILE: Optional[str] = Field(
        description="logging output file path",
        default=None,
    )

    # TESTED ON 2024-10-18 09:46 GMT
    LOG_FORMAT: str = Field(
        description="log format",
        default="%(asctime)s.%(msecs)03d %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s",
    )

    # TESTED ON 2024-10-18 09:47 GMT
    LOG_DATEFORMAT: Optional[str] = Field(
        description="log date format",
        default=None,
    )

    # TESTED ON 2024-10-18 09:48 GMT
    LOG_TZ: Optional[str] = Field(
        description="specify log timezone, eg: America/New_York",
        default=None,
    )

# TESTED ON 2024-10-18 09:50 GMT
class ModelLoadBalanceConfig(BaseSettings):
    """
    Model load balance configs
    """

    # TESTED ON 2024-10-18 09:51 GMT
    MODEL_LB_ENABLED: bool = Field(
        description="whether to enable model load balancing",
        default=False,
    )

# TESTED ON 2024-10-18 09:52 GMT
class BillingConfig(BaseSettings):
    """
    Platform Billing Configurations
    """

    # TESTED ON 2024-10-18 09:53 GMT
    BILLING_ENABLED: bool = Field(
        description="whether to enable billing",
        default=False,
    )

# TESTED ON 2024-10-18 09:54 GMT
class UpdateConfig(BaseSettings):
    """
    Update configs
    """

    # TESTED ON 2024-10-18 09:55 GMT
    CHECK_UPDATE_URL: str = Field(
        description="url for checking updates",
        default="",
    )

# TESTED ON 2024-10-18 09:56 GMT
class WorkflowConfig(BaseSettings):
    """
    Workflow feature configs
    """

    # TESTED ON 2024-10-18 09:57 GMT
    WORKFLOW_MAX_EXECUTION_STEPS: PositiveInt = Field(
        description="max execution steps in single workflow execution",
        default=500,
    )

    # TESTED ON 2024-10-18 09:58 GMT
    WORKFLOW_MAX_EXECUTION_TIME: PositiveInt = Field(
        description="max execution time in seconds in single workflow execution",
        default=1200,
    )

    # TESTED ON 2024-10-18 09:59 GMT
    WORKFLOW_CALL_MAX_DEPTH: PositiveInt = Field(
        description="max depth of calling in single workflow execution",
        default=5,
    )

    # TESTED ON 2024-10-18 10:00 GMT
    MAX_VARIABLE_SIZE: PositiveInt = Field(
        description="The maximum size in bytes of a variable. default to 5KB.",
        default=5 * 1024,
    )

# TESTED ON 2024-10-18 10:01 GMT
class OAuthConfig(BaseSettings):
    """
    oauth configs
    """

    # TESTED ON 2024-10-18 10:02 GMT
    OAUTH_REDIRECT_PATH: str = Field(
        description="redirect path for OAuth",
        default="/console/api/oauth/authorize",
    )

    # TESTED ON 2024-10-18 10:03 GMT
    GITHUB_CLIENT_ID: Optional[str] = Field(
        description="GitHub client id for OAuth",
        default=None,
    )

    # TESTED ON 2024-10-18 10:04 GMT
    GITHUB_CLIENT_SECRET: Optional[str] = Field(
        description="GitHub client secret key for OAuth",
        default=None,
    )

    # TESTED ON 2024-10-18 10:05 GMT
    GOOGLE_CLIENT_ID: Optional[str] = Field(
        description="Google client id for OAuth",
        default=None,
    )

    # TESTED ON 2024-10-18 10:06 GMT
    GOOGLE_CLIENT_SECRET: Optional[str] = Field(
        description="Google client secret key for OAuth",
        default=None,
    )

# TESTED ON 2024-10-18 22:43 GMT
class ModerationConfig(BaseSettings):
    """
    Moderation in app configs.
    """

    # TESTED ON 2024-10-18 22:44 GMT
    MODERATION_BUFFER_SIZE: PositiveInt = Field(
        description="buffer size for moderation",
        default=300,
    )


# TESTED ON 2024-10-18 22:45 GMT
class ToolConfig(BaseSettings):
    """
    Tool configs
    """

    # TESTED ON 2024-10-18 22:46 GMT
    TOOL_ICON_CACHE_MAX_AGE: PositiveInt = Field(
        description="max age in seconds for tool icon caching",
        default=3600,
    )

# TESTED ON 2024-10-18 22:47 GMT
class MailConfig(BaseSettings):
    """
    Mail Configurations
    """

    # TESTED ON 2024-10-18 22:48 GMT
    MAIL_TYPE: Optional[str] = Field(
        description="Mail provider type name, default to None, available values are `smtp` and `resend`.",
        default=None,
    )

    # TESTED ON 2024-10-18 22:49 GMT
    MAIL_DEFAULT_SEND_FROM: Optional[str] = Field(
        description="default email address for sending from ",
        default=None,
    )

    # TESTED ON 2024-10-18 22:50 GMT
    RESEND_API_KEY: Optional[str] = Field(
        description="API key for Resend",
        default=None,
    )

    # TESTED ON 2024-10-18 22:51 GMT
    RESEND_API_URL: Optional[str] = Field(
        description="API URL for Resend",
        default=None,
    )

    # TESTED ON 2024-10-18 22:54 GMT
    SMTP_SERVER: Optional[str] = Field(
        description="smtp server host",
        default=None,
    )

    # TESTED ON 2024-10-18 22:55 GMT
    SMTP_PORT: Optional[int] = Field(
        description="smtp server port",
        default=465,
    )

    # TESTED ON 2024-10-18 22:56 GMT
    SMTP_USERNAME: Optional[str] = Field(
        description="smtp server username",
        default=None,
    )

    # TESTED ON 2024-10-18 23:00 GMT
    SMTP_PASSWORD: Optional[str] = Field(
        description="smtp server password",
        default=None,
    )

    # TESTED ON 2024-10-18 23:01 GMT
    SMTP_USE_TLS: bool = Field(
        description="whether to use TLS connection to smtp server",
        default=False,
    )

    # TESTED ON 2024-10-18 23:02 GMT
    SMTP_OPPORTUNISTIC_TLS: bool = Field(
        description="whether to use opportunistic TLS connection to smtp server",
        default=False,
    )


# TESTED ON 2024-10-18 23:03 GMT
class RagEtlConfig(BaseSettings):
    """
    RAG ETL Configurations.
    """

    # TESTED ON 2024-10-18 23:04 GMT
    ETL_TYPE: str = Field(
        description="RAG ETL type name, default to `zerix`, available values are `zerix` and `Unstructured`. ",
        default="zerix",
    )

    # TESTED ON 2024-10-18 23:05 GMT
    KEYWORD_DATA_SOURCE_TYPE: str = Field(
        description="source type for keyword data, default to `database`, available values are `database` .",
        default="database",
    )

    # TESTED ON 2024-10-18 23:06 GMT
    UNSTRUCTURED_API_URL: Optional[str] = Field(
        description="API URL for Unstructured",
        default=None,
    )

    # TESTED ON 2024-10-18 23:07 GMT
    UNSTRUCTURED_API_KEY: Optional[str] = Field(
        description="API key for Unstructured",
        default=None,
    )


# TESTED ON 2024-10-18 23:12 GMT
class DataSetConfig(BaseSettings):
    """
    Dataset configs
    """

    # TESTED ON 2024-10-18 23:13 GMT
    CLEAN_DAY_SETTING: PositiveInt = Field(
        description="interval in days for cleaning up dataset",
        default=30,
    )

    # TESTED ON 2024-10-18 23:14 GMT
    DATASET_OPERATOR_ENABLED: bool = Field(
        description="whether to enable dataset operator",
        default=False,
    )


# TESTED ON 2024-10-18 23:09 GMT
class WorkspaceConfig(BaseSettings):
    """
    Workspace configs
    """

    # TESTED ON 2024-10-18 23:10 GMT
    INVITE_EXPIRY_HOURS: PositiveInt = Field(
        description="workspaces invitation expiration in hours",
        default=72,
    )


# TESTED ON 2024-10-18 23:11 GMT
class IndexingConfig(BaseSettings):
    """
    Indexing configs.
    """

    # TESTED ON 2024-10-18 23:12 GMT
    INDEXING_MAX_SEGMENTATION_TOKENS_LENGTH: PositiveInt = Field(
        description="max segmentation token length for indexing",
        default=1000,
    )

# TESTED ON 2024-10-18 23:13 GMT
class ImageFormatConfig(BaseSettings):
    # TESTED ON 2024-10-18 23:14 GMT
    MULTIMODAL_SEND_IMAGE_FORMAT: str = Field(
        description="multi model send image format, support base64, url, default is base64",
        default="base64",
    )


# TESTED ON 2024-10-18 23:15 GMT
class CeleryBeatConfig(BaseSettings):
    # TESTED ON 2024-10-18 23:16 GMT
    CELERY_BEAT_SCHEDULER_TIME: int = Field(
        description="the time of the celery scheduler, default to 1 day",
        default=1,
    )


# TESTED ON 2024-10-18 23:17 GMT
class PositionConfig(BaseSettings):
    # TESTED ON 2024-10-18 23:18 GMT
    POSITION_PROVIDER_PINS: str = Field(
        description="The heads of model providers",
        default="",
    )

    # TESTED ON 2024-10-18 23:19 GMT
    POSITION_PROVIDER_INCLUDES: str = Field(
        description="The included model providers",
        default="",
    )

    # TESTED ON 2024-10-18 23:20 GMT
    POSITION_PROVIDER_EXCLUDES: str = Field(
        description="The excluded model providers",
        default="",
    )

    # TESTED ON 2024-10-18 23:21 GMT
    POSITION_TOOL_PINS: str = Field(
        description="The heads of tools",
        default="",
    )

    # TESTED ON 2024-10-18 23:22 GMT
    POSITION_TOOL_INCLUDES: str = Field(
        description="The included tools",
        default="",
    )

    # TESTED ON 2024-10-18 23:23 GMT
    POSITION_TOOL_EXCLUDES: str = Field(
        description="The excluded tools",
        default="",
    )

    # TESTED ON 2024-10-18 23:21 GMT
    @computed_field
    def POSITION_PROVIDER_PINS_LIST(self) -> list[str]:
        return [item.strip() for item in self.POSITION_PROVIDER_PINS.split(",") if item.strip() != ""]

    # TESTED ON 2024-10-18 23:22 GMT
    @computed_field
    def POSITION_PROVIDER_INCLUDES_SET(self) -> set[str]:
        return {item.strip() for item in self.POSITION_PROVIDER_INCLUDES.split(",") if item.strip() != ""}

    # TESTED ON 2024-10-18 23:23 GMT
    @computed_field
    def POSITION_PROVIDER_EXCLUDES_SET(self) -> set[str]:
        return {item.strip() for item in self.POSITION_PROVIDER_EXCLUDES.split(",") if item.strip() != ""}

    # TESTED ON 2024-10-18 23:24 GMT
    @computed_field
    def POSITION_TOOL_PINS_LIST(self) -> list[str]:
        return [item.strip() for item in self.POSITION_TOOL_PINS.split(",") if item.strip() != ""]

    # TESTED ON 2024-10-18 23:25 GMT
    @computed_field
    def POSITION_TOOL_INCLUDES_SET(self) -> set[str]:
        return {item.strip() for item in self.POSITION_TOOL_INCLUDES.split(",") if item.strip() != ""}

    # TESTED ON 2024-10-18 23:26 GMT
    @computed_field
    def POSITION_TOOL_EXCLUDES_SET(self) -> set[str]:
        return {item.strip() for item in self.POSITION_TOOL_EXCLUDES.split(",") if item.strip() != ""}

# TESTED ON 2024-10-18 23:41 GMT
class FeatureConfig(
    # place the configs in alphabet order
    AppExecutionConfig,
    BillingConfig,
    CodeExecutionSandboxConfig,
    DataSetConfig,
    EndpointConfig,
    FileAccessConfig,
    FileUploadConfig,
    HttpConfig,
    ImageFormatConfig,
    InnerAPIConfig,
    IndexingConfig,
    LoggingConfig,
    MailConfig,
    ModelLoadBalanceConfig,
    ModerationConfig,
    OAuthConfig,
    RagEtlConfig,
    SecurityConfig,
    ToolConfig,
    UpdateConfig,
    WorkflowConfig,
    WorkspaceConfig,
    PositionConfig,
    # hosted services config
    HostedServiceConfig,
    CeleryBeatConfig,
):
    pass
