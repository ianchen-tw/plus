from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import depends

router = APIRouter()


# TODO: Rewrite use paged result
@router.get("/", response_model=List[schemas.College])
def get_list_of_colleges(
    db: Session = Depends(depends.get_db), skip: int = 0, limit: int = 100
) -> List[Any]:
    """ Get all information of all colleges"""
    colleges = crud.college.get_multi(db)
    return colleges


@router.post("/", response_model=schemas.College)
def create_college(
    *, db: Session = Depends(depends.get_db), college: schemas.CollegeCreate,
) -> Any:
    """
    Create College
    """
    c = crud.college.create(db=db, obj_in=college)
    return c


@router.get("/{college_id}", response_model=schemas.College)
def read_college_information(
    *, db: Session = Depends(depends.get_db), college_id: int,
) -> Any:
    """
    read college info
    """
    college = crud.college.get(db, id=college_id)
    if not college:
        raise HTTPException(
            status_code=404,
            detail="The college with this id does not exist in the system",
        )
    return college


@router.patch("/{college_id}", response_model=schemas.College)
def update_college(
    *,
    db: Session = Depends(depends.get_db),
    college_id: int,
    college_in: schemas.CollegeUpdate,
) -> Any:
    """
    Update fields of a college object.
    Will only update the field you prvide.
    """

    college = crud.college.get(db, id=college_id)
    if not college:
        raise HTTPException(
            status_code=404,
            detail="The college with this name does not exist in the system",
        )
    college = crud.college.update(db, db_obj=college, obj_in=college_in)
    return college


@router.delete("/{college_id}", response_model=schemas.College)
def remove_college(*, db: Session = Depends(depends.get_db), college_id: int,) -> Any:
    """
    [Dangerous] Remove a college object
    """

    college = crud.college.get(db, id=college_id)
    if not college:
        raise HTTPException(
            status_code=404,
            detail="The college with this name does not exist in the system",
        )
    college = crud.college.remove(db, id=college_id)
    return college
