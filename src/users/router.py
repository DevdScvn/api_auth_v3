
from typing import Annotated, Sequence

from alembic.util import status
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import get_current_user
from database import db_helper
from users.dao import UserDAO
from users.schemas import SUserOutput, SUserInput

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
async def get_all_users(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
        ) -> list[SUserOutput]:
    result = await UserDAO.find_all(session)
    return result


@router.get("/{user_id}")
async def get_user(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
                   user_id: int,
                   ) -> SUserOutput:
    result = await UserDAO.find_one_or_none(session, id=user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@router.get(
    "/profile/{user_id}",
)
async def read_users_me(
    current_user: Annotated[SUserOutput, Depends(get_current_user)],
    user_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SUserOutput:
    """
    Access user profile.

    If it's your own profile, you will see own data with more rights.
    Otherwise you will see just users data.
    """
    if user_id == current_user.id:
        return current_user
    return await UserDAO.get_user_by_id(session, user_id=user_id)
