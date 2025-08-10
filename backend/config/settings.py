from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """

    # MongoDB connection string
    mongodb_uri: str = ...
    database_name: str = ...
    gemini_api_key: str = ...
    host: str = "localhost"
    port: int = 8000

    project_name: str = "Interactive Story Weaver"
    project_version: str = "0.1.0"

    # Other settings can be added here as needed

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
