from typing import Annotated

from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from auth.auth import hash_user_password, authenticate_user, create_tokens, set_cookies
from auth.dao import AuthDAO
from auth.schemas import SUserRegister, Token
from database import db_helper
from settings.config import settings

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_409_CONFLICT: {"description": "User with this email already exists"}},
)
async def register_user(
    user_data: SUserRegister,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """
    Register a new user.

    Check if the user with the provided email already exists.
    If the user does not exist, hash the password and create a new user.
    """
    hashed_password = await hash_user_password(user_data)
    await AuthDAO.register_add(
        session, email=user_data.email, password=hashed_password, username=user_data.username
    )


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_401_UNAUTHORIZED: {"description": "Invalid credentials"}},
)
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Token:
    """
    Log in the user.

    If the user with the provided email and password exists, create access and refresh tokens.
    Refresh token will be stored in database.
    Both access and refresh tokens will be added to cookies.
    Return token values.
    """
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    tokens = await create_tokens(session, user)
    await set_cookies(response, tokens["access_token"], tokens["refresh_token"])
    return Token(**tokens, user_data=user)


@router.post(
    "/refresh",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_401_UNAUTHORIZED: {"description": "Invalid credentials"}},
)
async def refresh(request: Request, response: Response,
                  session: Annotated[AsyncSession, Depends(db_helper.session_getter)]) -> Token:
    """
    Refresh access token.
    Check if the refresh token is valid and exists in cookies.
    If the refresh token is valid, create new access and refresh tokens.
    Both access and refresh tokens will be added to cookies.
    Return token values.
    """
    wrong_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
    )
    if refresh_token := request.cookies.get("refresh_token"):
        try:
            payload = jwt.decode(
                refresh_token, settings.secret_key, algorithms=[settings.algorithm]
            )
            email: str = payload.get("sub")
        except JWTError:
            raise wrong_credentials from None
        user = await AuthDAO.find_one_or_none(session, email=email)
        new_tokens = await create_tokens(session, user)
        await set_cookies(response, new_tokens.get("access_token"), new_tokens.get("refresh_token"))
        return Token(**new_tokens, user_data=user)
    else:
        raise wrong_credentials


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(response: Response):
    """Log out the user. Remove access and refresh tokens from cookies."""
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")