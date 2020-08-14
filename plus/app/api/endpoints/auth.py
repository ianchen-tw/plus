from typing import Optional

from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from starlette.responses import Response

from app.core.auth import oauth_nctu, token

router = APIRouter()


@router.get("/nctu")
def user_auth():
    return oauth_nctu.user_auth()


@router.get("/nctu/redirect")
def user_profile(
    response: Response, profile: dict = Depends(oauth_nctu.fetch_user_profile)
):
    """User would be redirect to this page from auth server
    take their authorizatoin code to us
    and we could verify his/her profile by this code
    """
    jwt = token.create(profile)
    response.set_cookie("user", jwt, httponly=True)
    return {"msg": "Login to nctu oauth succeed!"}


@router.get("/")
def check_cookie(user: Optional[str] = Cookie(None)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
        )
    print(user)
    return {"user": token.verify(user)}
