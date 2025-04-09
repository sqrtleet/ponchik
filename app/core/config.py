from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    dbname: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

print(settings)