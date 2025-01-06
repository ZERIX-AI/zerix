from typing import Any, Optional
from urllib.parse import quote_plus

from pydantic import Field, NonNegativeInt, PositiveFloat, PositiveInt, computed_field
from pydantic_settings import BaseSettings

from configs.middleware.cache.redis_config import RedisConfig
from configs.middleware.storage.aliyun_oss_storage_config import AliyunOSSStorageConfig
from configs.middleware.storage.amazon_s3_storage_config import S3StorageConfig
from configs.middleware.storage.azure_blob_storage_config import AzureBlobStorageConfig
from configs.middleware.storage.google_cloud_storage_config import GoogleCloudStorageConfig
from configs.middleware.storage.huawei_obs_storage_config import HuaweiCloudOBSStorageConfig
from configs.middleware.storage.oci_storage_config import OCIStorageConfig
from configs.middleware.storage.tencent_cos_storage_config import TencentCloudCOSStorageConfig
from configs.middleware.storage.volcengine_tos_storage_config import VolcengineTOSStorageConfig
from configs.middleware.vdb.analyticdb_config import AnalyticdbConfig
from configs.middleware.vdb.chroma_config import ChromaConfig
from configs.middleware.vdb.elasticsearch_config import ElasticsearchConfig
from configs.middleware.vdb.milvus_config import MilvusConfig
from configs.middleware.vdb.myscale_config import MyScaleConfig
from configs.middleware.vdb.opensearch_config import OpenSearchConfig
from configs.middleware.vdb.oracle_config import OracleConfig
from configs.middleware.vdb.pgvector_config import PGVectorConfig
from configs.middleware.vdb.pgvectors_config import PGVectoRSConfig
from configs.middleware.vdb.qdrant_config import QdrantConfig
from configs.middleware.vdb.relyt_config import RelytConfig
from configs.middleware.vdb.tencent_vector_config import TencentVectorDBConfig
from configs.middleware.vdb.tidb_vector_config import TiDBVectorConfig
from configs.middleware.vdb.weaviate_config import WeaviateConfig


# TESTED ON 2024-10-19 00:28 GMT
class StorageConfig(BaseSettings):
    # TESTED ON 2024-10-19 00:29 GMT
    STORAGE_TYPE: str = Field(
        description="storage type,"
        " default to `local`,"
        " available values are `local`, `s3`, `azure-blob`, `aliyun-oss`, `google-storage`.",
        default="local",
    )

    # TESTED ON 2024-10-19 00:30 GMT
    STORAGE_LOCAL_PATH: str = Field(
        description="local storage path",
        default="storage",
    )

# TESTED ON 2024-10-19 00:31 GMT
class VectorStoreConfig(BaseSettings):
    # TESTED ON 2024-10-19 00:32 GMT
    VECTOR_STORE: Optional[str] = Field(
        description="vector store type",
        default=None,
    )

# TESTED ON 2024-10-19 00:33 GMT
class KeywordStoreConfig(BaseSettings):
    # TESTED ON 2024-10-19 00:34 GMT
    KEYWORD_STORE: str = Field(
        description="keyword store type",
        default="jieba",
    )

# TESTED ON 2024-10-19 01:11 GMT    
class DatabaseConfig:
    # TESTED ON 2024-10-19 01:12 GMT
    DB_HOST: str = Field(
        description="db host",
        default="localhost",
    )

    # TESTED ON 2024-10-19 01:13 GMT
    DB_PORT: PositiveInt = Field(
        description="db port",
        default=5432,
    )

    # TESTED ON 2024-10-19 01:14 GMT
    DB_USERNAME: str = Field(
        description="db username",
        default="postgres",
    )

    # TESTED ON 2024-10-19 01:15 GMT
    DB_PASSWORD: str = Field(
        description="db password",
        default="",
    )

    # TESTED ON 2024-10-19 01:16 GMT
    DB_DATABASE: str = Field(
        description="db database",
        default="zerix",
    )

    # TESTED ON 2024-10-19 01:17 GMT
    DB_CHARSET: str = Field(
        description="db charset",
        default="",
    )

    # TESTED ON 2024-10-19 01:18 GMT
    DB_EXTRAS: str = Field(
        description="db extras options. Example: keepalives_idle=60&keepalives=1",
        default="",
    )

    # TESTED ON 2024-10-19 01:19 GMT
    SQLALCHEMY_DATABASE_URI_SCHEME: str = Field(
        description="db uri scheme",
        default="postgresql",
    )

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        db_extras = (
            f"{self.DB_EXTRAS}&client_encoding={self.DB_CHARSET}" if self.DB_CHARSET else self.DB_EXTRAS
        ).strip("&")
        db_extras = f"?{db_extras}" if db_extras else ""
        return (
            f"{self.SQLALCHEMY_DATABASE_URI_SCHEME}://"
            f"{quote_plus(self.DB_USERNAME)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"
            f"{db_extras}"
        )

    # TESTED ON 2024-10-19 02:54 GMT
    SQLALCHEMY_POOL_SIZE: NonNegativeInt = Field(
        description="pool size of SqlAlchemy",
        default=30,
    )

    # TESTED ON 2024-10-19 02:55 GMT
    SQLALCHEMY_MAX_OVERFLOW: NonNegativeInt = Field(
        description="max overflows for SqlAlchemy",
        default=10,
    )

    # TESTED ON 2024-10-19 02:56 GMT
    SQLALCHEMY_POOL_RECYCLE: NonNegativeInt = Field(
        description="SqlAlchemy pool recycle",
        default=3600,
    )

    # TESTED ON 2024-10-19 02:57 GMT
    SQLALCHEMY_POOL_PRE_PING: bool = Field(
        description="whether to enable pool pre-ping in SqlAlchemy",
        default=False,
    )

    # TESTED ON 2024-10-19 02:58 GMT
    SQLALCHEMY_ECHO: bool | str = Field(
        description="whether to enable SqlAlchemy echo",
        default=False,
    )

    # TESTED ON 2024-10-19 02:59 GMT
    @computed_field
    @property
    def SQLALCHEMY_ENGINE_OPTIONS(self) -> dict[str, Any]:
        return {
            "pool_size": self.SQLALCHEMY_POOL_SIZE,
            "max_overflow": self.SQLALCHEMY_MAX_OVERFLOW,
            "pool_recycle": self.SQLALCHEMY_POOL_RECYCLE,
            "pool_pre_ping": self.SQLALCHEMY_POOL_PRE_PING,
            "connect_args": {"options": "-c timezone=UTC"},
        }

# TESTED ON 2024-10-19 03:05 GMT
class CeleryConfig(DatabaseConfig):
    # TESTED ON 2024-10-19 03:06 GMT
    CELERY_BACKEND: str = Field(
        description="Celery backend, available values are `database`, `redis`",
        default="database",
    )

    # TESTED ON 2024-10-19 03:07 GMT
    CELERY_BROKER_URL: Optional[str] = Field(
        description="CELERY_BROKER_URL",
        default=None,
    )

    # TESTED ON 2024-10-19 03:08 GMT
    CELERY_USE_SENTINEL: Optional[bool] = Field(
        description="Whether to use Redis Sentinel mode",
        default=False,
    )

    # TESTED ON 2024-10-19 03:09 GMT
    CELERY_SENTINEL_MASTER_NAME: Optional[str] = Field(
        description="Redis Sentinel master name",
        default=None,
    )

    # TESTED ON 2024-10-19 03:10 GMT
    CELERY_SENTINEL_SOCKET_TIMEOUT: Optional[PositiveFloat] = Field(
        description="Redis Sentinel socket timeout",
        default=0.1,
    )

    # TESTED ON 2024-10-19 03:11 GMT
    @computed_field
    @property
    def CELERY_RESULT_BACKEND(self) -> str | None:
        return (
            "db+{}".format(self.SQLALCHEMY_DATABASE_URI)
            if self.CELERY_BACKEND == "database"
            else self.CELERY_BROKER_URL
        )

    # TESTED ON 2024-10-19 03:12 GMT
    @computed_field
    @property
    def BROKER_USE_SSL(self) -> bool:
        return self.CELERY_BROKER_URL.startswith("rediss://") if self.CELERY_BROKER_URL else False

# TESTED ON 2024-10-19 03:17 GMT
class MiddlewareConfig(
    # place the configs in alphabet order
    CeleryConfig,
    DatabaseConfig,
    KeywordStoreConfig,
    RedisConfig,
    # configs of storage and storage providers
    StorageConfig,
    AliyunOSSStorageConfig,
    AzureBlobStorageConfig,
    GoogleCloudStorageConfig,
    TencentCloudCOSStorageConfig,
    HuaweiCloudOBSStorageConfig,
    VolcengineTOSStorageConfig,
    S3StorageConfig,
    OCIStorageConfig,
    # configs of vdb and vdb providers
    VectorStoreConfig,
    AnalyticdbConfig,
    ChromaConfig,
    MilvusConfig,
    MyScaleConfig,
    OpenSearchConfig,
    OracleConfig,
    PGVectorConfig,
    PGVectoRSConfig,
    QdrantConfig,
    RelytConfig,
    TencentVectorDBConfig,
    TiDBVectorConfig,
    WeaviateConfig,
    ElasticsearchConfig,
):
    pass
