from configs.extra.notion_config import NotionConfig
from configs.extra.sentry_config import SentryConfig


# TESTED ON 2024-10-19 03:27 GMT
class ExtraServiceConfig(
    # place the configs in alphabet order
    NotionConfig,
    SentryConfig,
):
    pass
