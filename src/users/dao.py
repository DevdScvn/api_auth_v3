from sqlalchemy.ext.asyncio import AsyncSession

from dao.dao import BaseDAO
from users.models import User
from users.schemas import SUserOutput


class UserDAO(BaseDAO):
    model = User

    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int) -> SUserOutput:
        """Return user by id."""
        return await UserDAO.get_object_or_404(session, id=user_id)