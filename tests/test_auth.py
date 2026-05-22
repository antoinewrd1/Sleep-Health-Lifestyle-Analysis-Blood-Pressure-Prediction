import pytest
from fastapi import HTTPException

from src.auth.security import verify_api_key


def test_verify_api_key_accepts_valid_key():
    assert verify_api_key("dev-secret-key") is True


def test_verify_api_key_rejects_invalid_key():
    with pytest.raises(HTTPException):
        verify_api_key("wrong-key")