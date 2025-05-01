from pydantic import BaseModel, EmailStr

from users.schemas import SUserOutput


class SUserRegister(BaseModel):

    email: EmailStr
    password: str
    username: str


class SUserLogin(BaseModel):

    email: EmailStr
    password: str


class STokens(BaseModel):

    access_token: str
    refresh_token: str


class TokenData(BaseModel):

    email: str


class Token(BaseModel):
    """Token pair schema."""

    access_token: str
    refresh_token: str | None
    token_type: str
    user_data: SUserOutput