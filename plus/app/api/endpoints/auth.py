from typing import Optional

from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from app import crud
from app.api import depends
from app.core.auth import oauth_nctu, token

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
    # if profile not in db
    # create one and set_cookie (user_id)
    sid = profile.get("username")
    if sid is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="OAuth failed"
        )
    user = crud.user.find_by_student_id(db, student_id=sid)
    if user is None:
        user = crud.user.create(
            db=db,
            obj_in={"student_id": sid, "email": profile.get("email")},
        )
    else:
        print("user exists!")
    to_encode = {"uid": user.id}
    jwt = token.create(to_encode)
    response.set_cookie("user", jwt, httponly=True)
    return {"msg": "Login to nctu oauth succeed!"}


@router.get("/")
def check_cookie(*, db: Session = Depends(depends.get_db), user: Optional[str] = Cookie(None)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password"
        )
    uid = token.verify(user)
    user = crud.user.get(db, id=uid)
    return {"user": uid, "email": user.email}
