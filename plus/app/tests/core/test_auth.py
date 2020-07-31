import os
from typing import Dict

from app.core.auth import OAuth2


class MockedResponse:
    def __init__(self, data: Dict):
        self.data = data

    def json(self):
        return self.data


def gen_Oauth2(prefix=None):
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


def test_get_user_token(client, mocker):
    def mock_fetch_token(self, url, data):
        assert url == "https://id.nctu.edu.tw/o/token/"
        res = {"access_token": "TEST_TOKEN-9487"}
        return MockedResponse(res)

    mocker.patch("app.core.auth.AuthServerController.fetch_user_token", mock_fetch_token)
    oauth = gen_Oauth2(prefix="NCTU_OAUTH")
    res = oauth._get_user_token(code=8787)
    print(f"res = {res}")
