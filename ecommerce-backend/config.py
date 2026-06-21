from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./ecommerce.db"
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 43200
    RESEND_API_KEY: str = "re_xxxxxxxxx"  # REPLACE WITH YOUR KEY
    FROM_EMAIL: str = "onboarding@resend.dev"
    ALLOWED_ORIGINS: list = ["http://localhost:5173", "http://localhost:3000"]
    
    class Config:
        env_file = ".env"

settings = Settings()
