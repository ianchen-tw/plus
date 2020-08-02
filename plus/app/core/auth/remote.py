from typing import Dict

import requests


class AuthServerController:
    def fetch_user_token(self, token_url: str, post_data: Dict):
        return requests.post(token_url, data=post_data)

    def fetch_user_profile(self, data_url: str, headers: Dict):
        return requests.get(data_url, headers=headers)
