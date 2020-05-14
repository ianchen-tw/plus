from pydantic import BaseSettings

# TODO: provide a description of this page
class Settings(BaseSettings):
    API_V1_STR = "/api/v1"
    PROJECT_NAME: str

    class Config:
        case_sensitive = True


settings = Settings(_env_file="dev.env")
