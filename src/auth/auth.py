import datetime
from typing import Annotated

from fastapi import Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from auth.dao import AuthDAO, RefreshTokenDAO
from auth.schemas import SUserLogin, SUserRegister, TokenData
from database import db_helper
from settings.config import settings
from users.models import User
from users.schemas import SUserOutput

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# async def check_user_exists(session: AsyncSession, email: str) -> bool:
#     check_existing_user = await AuthDAO.find_one_or_none(session, email=email)
#     if check_existing_user:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists"
#         )


async def hash_user_password(user_data: SUserRegister) -> str:
    return get_password_hash(user_data.password)


async def authenticate_user(session: AsyncSession, email, password) -> SUserLogin:
    user = await AuthDAO.find_one_or_none(session, email=email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user


def create_access_token(data: dict, expires_delta: datetime.timedelta | None = None):
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: datetime.timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


async def create_tokens(session: AsyncSession, user: User) -> dict:
    access_token_expires = datetime.timedelta(minutes=settings.access_token)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    refresh_token_expires = datetime.timedelta(days=settings.refresh_token)
    refresh_token = create_refresh_token(
        data={"sub": user.email}, expires_delta=refresh_token_expires
    )
    await RefreshTokenDAO.register_add(
        session=session,
        user_id=user.id,
        token=refresh_token,
        expires_at=datetime.datetime.now(datetime.timezone.utc) + refresh_token_expires,
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


async def set_cookies(response: Response, access_token: str, refresh_token: str):
    """Set the access token and refresh token as cookies."""
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=settings.access_token,
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=settings.refresh_token,
    )


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SUserOutput:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception from None
    user = await AuthDAO.find_one_or_none(session, email=token_data.email)
    if not user:
        raise credentials_exception
    return SUserOutput.model_validate(user)


# def create_email_verification_token(
#     email: str,
#     expires_delta: datetime.timedelta = datetime.timedelta(
#         hours=1
#     ),
# ) -> str:
#     """Create a token for email verification."""
#     payload = {
#         "sub": email,
#         "verify": True,
#         "exp": datetime.datetime.now(datetime.timezone.utc) + expires_delta,
#     }
#     return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


# async def send_verification_email(email: str, token: str) -> None:
#     """Send email with the verification token."""
#     verification_link = f"{settings.VERIFICATION_URL}/{token}"
#     email_body = render_verification_email(email, verification_link)
#     await send_email(email, f"Email Verification for {settings.PROJECT_NAME}", email_body)


# async def register_user(
#     session: AsyncSession,
#         user_data: SUserRegister,
#         background_tasks: BackgroundTasks
# ) -> SUserOutput:
#     """Register a new user."""
#     await check_user_exists(session, user_data.email)
#     hashed_password = await hash_user_password(user_data)
#     await AuthDAO.register_add(
#         session, email=user_data.email, password=hashed_password, username=user_data.username
#     )
#     token = create_email_verification_token(user_data.email)
#     background_tasks.add_task(
#         send_verification_email,
#         user_data.email,
#         token,
#     )
