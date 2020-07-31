import logging
import os
import pprint

import requests
from fastapi.responses import RedirectResponse

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def os_getenv(value):
    env = os.getenv(value)
    if env is None:
        # FIXME self-defined exception?
        raise Exception("ENV", value, "not exists!")
    return env


class OAuth2:
    def __init__(self, auth_prefix: str):
        config_fields = [
            "client_id",
            "client_secret",
            "auth_url",
            "token_url",
            "data_url",
            "redirect_url",
        ]
        cfg = [f"{auth_prefix}_{field}".upper() for field in config_fields]
        self.config = {}
        for i, field in enumerate(cfg):
            try:
                value = os_getenv(field)
                self.config[config_fields[i]] = value
            except Exception as err:
                logger.error(err)
                raise err

    def user_auth(self):
        """Redirect the user to third party auth page
        """
        return RedirectResponse(self.config["auth_url"])

    def redeem_token(self, code):
        """redirect_url get code and use it to redeem the token
        """
        body = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
            "redirect_uri": self.config["redirect_url"],
        }
        res = requests.post(self.config["token_url"], data=body).json()
        return self.acquire_data(res["access_token"])

    def acquire_data(self, access_token):
        header = {"Authorization": "Bearer " + access_token}
        res = requests.get(self.config["data_url"], headers=header).json()
        return res

    def print_config(self):
        pp = pprint.PrettyPrinter()
        pp.pprint(self.config)


def nctu():
    auth = OAuth2("nctu")
    return auth
