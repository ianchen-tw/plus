from app.core.config import settings
from .oauth2 import OAuth2

oauth_nctu = OAuth2(**settings.OAUTH_NCTU.dict())

__all__ = ["oauth_nctu"]
