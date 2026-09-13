import os

from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
VALID_ENVIRONMENTS = {"dev", "test", "prod"}

def validate_environment():
    if ENVIRONMENT not in VALID_ENVIRONMENTS:
        raise ValueError(
            f"Invalid environment: {ENVIRONMENT}"
            f"Expected one of: {VALID_ENVIRONMENTS}"
        )

BASE_URL = os.getenv("BASE_URL", "https://api.example.com")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "5"))
API_USERNAME = os.getenv("API_USERNAME", "")
API_PASSWORD = os.getenv("API_PASSWORD", "")


