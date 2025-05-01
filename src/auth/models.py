import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, DateTime, false
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import TimeStampModel

if TYPE_CHECKING:
    from users.models import User


class RefreshToken(TimeStampModel):


    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    token: Mapped[str] = mapped_column()
    expires_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    revoked: Mapped[bool] = mapped_column(server_default=false())

    user: Mapped["User"] = relationship("User", back_populates="refresh_tokens")

    def __repr__(self) -> str:
        return f"RefreshToken(id={self.id!r}, related_user={self.user_id!r})"

    def __str__(self) -> str:
        return f"RefreshToken(id={self.id}, related_user={self.user_id})"