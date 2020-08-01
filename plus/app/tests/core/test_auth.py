import os
from typing import Dict

from app.core.auth import OAuth2
from app.tests.utils import fake


class MockedResponse:
    def __init__(self, data: Dict):
        self.data = data

    def json(self):
        return self.data


def gen_oauth2(prefix=None):
    def env(field: str):
        return os.getenv(f"{prefix}_{field}".upper())

    fields = [
        "client_id",
        "client_secret",
        "auth_url",
        "token_url",
        "data_url",
        "redirect_url",
    ]
    args = {f: env(f) for f in fields}
    return OAuth2(**args)


def test_NCTU_get_user_token(client, mocker):
    mock_method_called = False
    expect_access_token = "TEST_TOKEN-9487"

    def mock_fetch_token(self, url, data):
        """Specified in nctu_oauth
        """
        nonlocal mock_method_called
        mock_method_called = True
        res = {
            "access_token": expect_access_token,
            "token_type": "Bearer",
            "expires_in": 36000,
            "scope": "profile",
            "refresh_token": "test_refresh_token",
        }
        return MockedResponse(res)

    mocker.patch("app.core.auth.AuthServerController.fetch_user_token", mock_fetch_token)
    oauth = gen_oauth2(prefix="NCTU_OAUTH")
    token = oauth._get_user_token(code="TEST_USER_CODE")

    assert mock_method_called == True
    assert token == expect_access_token


def test_NCTU_get_user_profile(client, mocker):
    mock_method_called = False
    expect_email = f"{fake.user_name}@cs08g@nctu.edu.tw"

    def mock_fetch_profile(self, url, headers):
        """Specified in nctu_oauth
        """
        nonlocal mock_method_called
        mock_method_called = True
        res = {"username": "0856039", "email": expect_email}
        return MockedResponse(res)

    mocker.patch(
        "app.core.auth.AuthServerController.fetch_user_profile", mock_fetch_profile
    )
    oauth = gen_oauth2(prefix="NCTU_OAUTH")
    data = oauth._get_user_profile(access_token="TEST_ACCESS_TOKEN")

    assert mock_method_called == True
    assert data["email"] == expect_email
