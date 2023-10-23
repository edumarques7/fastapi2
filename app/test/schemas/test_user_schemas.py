import pytest
from datetime import datetime
from app.schemas.user import User, TokenData


def test_user_schema():
    user = User(username='Eduardo', password='pass#')
    assert user.dict() == {
        'username': 'Eduardo',
        'password': 'pass#'
    }


def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='João#', password='pass#')


def test_token_date():
    expires_at = datetime.now()
    token_data = TokenData(
        access_token='token qualquer',
        expires_at = expires_at
    )

    assert token_data.dict() == {
        'access_token': 'token qualquer',
        'expires_at': expires_at
    }