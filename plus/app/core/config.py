import logging
import os
from typing import Any, Dict, Optional

from pydantic import AnyHttpUrl, BaseModel, BaseSettings, PostgresDsn, validator

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


class OauthConfig(BaseModel):
    client_id: str
    client_secret: str
    auth_url: AnyHttpUrl
    token_url: AnyHttpUrl
    data_url: AnyHttpUrl
    redirect_url: AnyHttpUrl


# TODO: provide a description of this page
class Settings(BaseSettings):
    API_V1_STR = "/api/v1"
    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:  # noqa
        if isinstance(v, str):
            return v
        # build SQLALCHEMY_DATABASE_URI from environment variables
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    OAUTH_NCTU: Optional[OauthConfig] = None

    @validator("OAUTH_NCTU", pre=True)
    def build_and_validate_nctu_auth(cls, v, values, **kwargs) -> Any:
        prefix = "NCTU_OAUTH"

        def env(field: str):
            return os.getenv(f"{prefix}_{field}".upper())

        fields = [
            "client_id",
            "client_secret",
            "auth_url",
            "token_url",
            "data_url",
            "redirect_url",
        ]
        configs = {f: env(f) for f in fields}
        return OauthConfig(**configs)

    class Config:
        case_sensitive = True


settings = Settings()
