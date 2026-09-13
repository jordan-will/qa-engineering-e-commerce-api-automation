import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://api.example.com")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "5"))
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
API_USERNAME = os.getenv("API_USERNAME", "")
API_PASSWORD = os.getenv("API_PASSWORD", "")