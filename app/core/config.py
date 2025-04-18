from pydantic_settings import BaseSettings
from typing import ClassVar


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    jwt_secret: str
    jwt_algorithm: ClassVar[str] = "HS256"
    jwt_expiration_minutes: int = 60

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

print(settings)
