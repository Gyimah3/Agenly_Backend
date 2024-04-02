from pydantic_settings import BaseSettings


# class Settings(BaseSettings):
#     database_url: str = "postgresql://postgres.usrzavfdhnyprrhxfhkz:sconzylize123*@aws-0-us-east-1.pooler.supabase.com:5432/postgres"
#     secret_key: str = "sSMIcPCi99QQ4udIgmdvn5SdjkMYmo1L_yjL5y59FiQ"
#     algorithm: str = "HS256"
#     access_token_expire_minutes: int = 60  # 60 minutes

#     class Config:
#         env_file = ".env"

# settings = Settings()

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
