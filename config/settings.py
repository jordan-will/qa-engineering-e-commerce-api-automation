import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
    VALID_ENVIRONMENTS = {"dev", "test", "prod"}

    BASE_URL = os.getenv("BASE_URL", "https://api.example.com")
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "5"))
    API_USERNAME = os.getenv("API_USERNAME", "")
    API_PASSWORD = os.getenv("API_PASSWORD", "")

    def validate_environment(self):
        if self.ENVIRONMENT not in self.VALID_ENVIRONMENTS:
            raise ValueError(
                f"Invalid environment: {self.ENVIRONMENT}"
                f"Expected one of: {self.VALID_ENVIRONMENTS}"
            )


settings = Settings()


