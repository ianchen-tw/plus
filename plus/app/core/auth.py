from typing import Dict

import requests
from fastapi.responses import RedirectResponse

from app.core.config import settings


class AuthServerController:
    def fetch_user_token(self, token_url: str, post_data: Dict):
        return requests.post(self.token_url, data=post_data)

    def fetch_user_data(self, data_url, headers):
        return requests.get(data_url, headers=headers)


class OAuth2:
    def __init__(
        self,
        client_id,
        client_secret,
        auth_url,
        token_url,
        data_url,
        redirect_url,
        scope="",
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.token_url = token_url
        self.data_url = data_url
        self.redirect_url = redirect_url
        self.scope = scope

        self.auth_server = AuthServerController()

    def user_auth(self):
        """Redirect the user to third party auth page
        the auth_url contains our registered id, which would let the auth server knows
        that it's us to require access to this user,
        once the user logged in successfully in the auth server, the auth server would grant access right to us
        """
        return RedirectResponse(self.auth_url)

    # TODO: add type hint
    def fetch_user_data(self, code: str):
        access_token = self.__get_user_token(code)
        data = self.__get_user_data(access_token)
        return data

    # TODO: add type hint
    def _get_user_token(self, code) -> str:
        """redirect_url catch code and use it to redeem the token
        """
        post_data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_url,
        }
        res = self.auth_server.fetch_user_token(self.token_url, post_data).json()
        print(f"res {res}")
        return res.get("access_token")

    # TODO: add type hint
    def _get_user_data(self, access_token: str):
        headers = {"Authorization": f"Bearer {access_token}"}
        res = self.auth_server.fetch_user_data(self.data_url, headers).json()
        return res


oauth_nctu = OAuth2(**settings.OAUTH_NCTU.dict())
