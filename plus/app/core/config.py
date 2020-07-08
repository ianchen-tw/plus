from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


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

    class Config:
        case_sensitive = True


settings = Settings()
