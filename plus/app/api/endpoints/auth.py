from fastapi import APIRouter

from app.core.auth import oauth_nctu

router = APIRouter()


@router.get("/nctu")
def user_auth():
    return oauth_nctu.user_auth()


@router.get("/nctu/redirect")
def user_profile(code: str):
    """User would be redirect to this page from auth server
    take their authorizatoin code to us
    and we could verify his/her data by this code
    """
    data = oauth_nctu.fetch_user_profile(code)
    print("Get user data")
    print(data, flush=True)
    return "Login to nctu oauth succeed!"
