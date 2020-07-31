import os

from fastapi import APIRouter

from app.core import OAuth2

router = APIRouter()

nctu_oauth = OAuth2.OAuth2(
    client_id=os.getenv("NCTU_CLIENT_ID"),
    client_secret=os.getenv("NCTU_CLIENT_SECRET"),
    auth_url=os.getenv("NCTU_AUTH_URL"),
    token_url=os.getenv("NCTU_TOKEN_URL"),
    data_url=os.getenv("NCTU_DATA_URL"),
    redirect_url=os.getenv("NCTU_REDIRECT_URL"),
)


@router.get("/nctu")
def user_auth():
    return nctu_oauth.user_auth()


@router.get("/nctu/redirect")
def user_data(code: str):
    res = nctu_oauth.user_data(code)
    print(res)
    return "Login to nctu oauth succeed!"
