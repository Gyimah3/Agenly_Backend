from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres.usrzavfdhnyprrhxfhkz:sconzylize123*@aws-0-us-east-1.pooler.supabase.com:5432/postgres"
    secret_key: str = "sSMIcPCi99QQ4udIgmdvn5SdjkMYmo1L_yjL5y59FiQ"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60  # 60 minutes

    class Config:
        env_file = ".env"

settings = Settings()
