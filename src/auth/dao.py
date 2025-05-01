from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import RefreshToken
from dao.dao import BaseDAO
from users.models import User


class AuthDAO(BaseDAO):
    model = User


class RefreshTokenDAO(BaseDAO):
    model = RefreshToken

    @classmethod
    async def get_last_token(cls, session: AsyncSession, user_id: int, order_by, limit: int) -> dict:
        """Get the last token for the user based on the order_by column."""
        query = select(cls.model.__table__.columns).order_by(desc(order_by)).limit(limit)
        result = await session.execute(query)
        return result.mappings().one_or_none()
