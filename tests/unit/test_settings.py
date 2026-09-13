import pytest
from config.settings import settings

def test_valid_environment():
    settings.validate_environment()

def test_invalid_environment():
    original_environment = settings.ENVIRONMENT
    settings.ENVIRONMENT = "staging"

    try:
        with pytest.raises(ValueError):
            settings.validate_environment()
    finally:
        settings.ENVIRONMENT = original_environment

def test_default_settings():
    assert settings.BASE_URL == "https://api.example.com"
    assert settings.REQUEST_TIMEOUT == 5
    assert settings.ENVIRONMENT == "dev"

    