from pydantic_settings import BaseSettings
from typing import Any
import os

#Constants from environment variables
USERPOOL_REGION = os.environ.get("USERPOOL_REGION")
USERPOOL_ID = os.environ.get("USERPOOL_ID")
APP_CLIENT_ID = os.environ.get("APP_CLIENT_ID")

class Settings(BaseSettings):
    check_expiration: bool = True
    jwt_header_prefix: str = "Bearer"
    jwt_header_name: str = "Authorization"
    userpools: dict[str, dict[str, Any]] = {
    
        "eu": {
            "region": "USERPOOL_REGION",
            "userpool_id": "USERPOOL_ID",
            "app_client_id": ["APP_CLIENT_ID_1", "APP_CLIENT_ID_2"] # Example with multiple ids
        },
        "petfinder-userpool": {
            "region": "USERPOOL_REGION",
            "userpool_id": "USERPOOL_ID",
            "app_client_id": "APP_CLIENT_ID"
        },
        
    }

settings = Settings()