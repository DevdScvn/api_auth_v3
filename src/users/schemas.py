from pydantic import BaseModel


class SUserInput(BaseModel):

    email: str
    password: str


class SUserOutput(BaseModel):

    id: int
    email: str
    username: str
    is_admin: bool
    is_verified: bool