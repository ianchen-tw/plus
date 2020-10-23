from app.core.config import settings
from .oauth2 import OAuth2
from .token import Token

oauth_nctu = OAuth2(**settings.OAUTH_NCTU.dict())
token = Token(**settings.JWT.dict())

__all__ = ["oauth_nctu"]
