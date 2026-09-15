import pytest

from src.models.user import User
from src.utils.data_loader import load_json, load_model

USER_FILE = "tests/data/users.json"

def test_load_json():
    data = load_json(USER_FILE)

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "John Doe"

def test_load_model():
    users = load_model(USER_FILE, User)

    assert isinstance(users, list)
    assert len(users) == 2
    assert all(isinstance(user, User) for user in users)