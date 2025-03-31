from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str = ""
    database_hostname: str
    database_password: str
    database_port: int
    database_username: str
    database_name: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
