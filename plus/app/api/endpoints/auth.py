from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.api import depends
from app.core.auth import oauth_nctu, token
from app.core.auth.user import UserHandler

router = APIRouter()


@router.get("/nctu")
def user_auth():
    return oauth_nctu.user_auth()


@router.get("/nctu/redirect")
def user_profile(
    *,
    db: Session = Depends(depends.get_db),
    response: Response,
    profile: dict = Depends(oauth_nctu.fetch_user_profile)
):
    """User would be redirect to this page from auth server
    take their authorizatoin code to us
    and we could verify his/her profile by this code
    """
    sid = profile.get("username")
    email = profile.get("email")
    if sid is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="nctu OAuth failed"
        )
    user_handler = UserHandler(db)
    user = user_handler.create_user_if_not_exist(sid, email)
    to_encode = {"uid": user.id}
    jwt = token.create(to_encode)
    response.set_cookie("user", jwt, httponly=True)
    return {"msg": "Login to nctu oauth succeed!"}


# @router.get("/")
# def check_cookie(
#     *, db: Session = Depends(depends.get_db), user: Optional[str] = Cookie(None)
# ):
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
#         )
#     uid = token.verify(user)
#     user = crud.user.get(db, id=uid)
#     return {"user": uid, "email": user.email}
