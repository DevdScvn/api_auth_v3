from typing import List, TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import TimeStampModel
if TYPE_CHECKING:
    from auth.models import RefreshToken

class User(TimeStampModel):

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[EmailStr] = mapped_column(String(256), unique=True)
    username: Mapped[str] = mapped_column(String(256), unique=True)
    password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    refresh_tokens: Mapped[List["RefreshToken"]] = relationship(
        "RefreshToken",
        cascade="all, delete",
        back_populates="user",
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"

    def __str__(self) -> str:
        return f"User(id={self.id}, email={self.email})"