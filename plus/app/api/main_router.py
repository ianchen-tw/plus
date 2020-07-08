import logging

from fastapi import APIRouter, status

from app.api.endpoints import college, users

logger = logging.getLogger(__name__)

main_router = APIRouter()


def include_routers():
    global main_router
    main_router.include_router(users.router, prefix="/users", tags=["users"])
    main_router.include_router(college.router, prefix="/college", tags=["college"])


@main_router.get(
    "/",
    tags=["example"],
    responses={
        status.HTTP_200_OK: {
            "description": "HTTP_200_OK have no description",
            "content": {"application/json": {"example": {"message": "some words"}}},
        },
        status.HTTP_403_FORBIDDEN: {"description": "a example for 403 response"},
    },
)
def function_name_would_become_title(prerequisite: str = "No",):
    """ This endpoint served as an example for writing self documented API code.

    What you wrote in the code **will be** exposed to the world
    throught out the [docstring](https://realpython.com/documenting-python-code/#commenting-vs-documenting-code).

    ### Happy Coding!
    """
    logger.info("[GET] a example logger event")
    if prerequisite != "No":
        return {"message": "you must be kidding"}
    return {"message": "It works!"}


include_routers()
