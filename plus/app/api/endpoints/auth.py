import logging

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.core import OAuth2

router = APIRouter()
nctu_oauth = OAuth2.nctu()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/nctu")
def user_auth():
    return nctu_oauth.user_auth()


@router.get("/nctu/redirect")
def user_data(code: str):
    res = nctu_oauth.redeem_token(code)
    logger.info("user logon")
    logger.info(res)
    return RedirectResponse("/")
