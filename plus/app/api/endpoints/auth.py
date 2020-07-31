from fastapi import APIRouter

from app.core.auth import oauth_nctu

router = APIRouter()


@router.get("/nctu")
def user_auth():
    return oauth_nctu.user_auth()


@router.get("/nctu/redirect")
def user_data(code: str):
    """User would be redirect to this page from auth server
    take their authorizatoin code to us
    and we could verify his/her data by this code
    """
    res = oauth_nctu.user_data(code)
    print(res)
    return "Login to nctu oauth succeed!"
