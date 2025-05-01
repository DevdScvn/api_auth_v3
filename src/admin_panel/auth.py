from fastapi import HTTPException
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from database import db_helper
from src.auth.auth import authenticate_user, create_tokens, get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        async with db_helper.session_factory() as session:
            form = await request.form()
            email, password = form["username"], form["password"]
            try:
                user = await authenticate_user(session, email, password)
            except HTTPException:
                return False
            tokens = await create_tokens(session, user)
            request.session.update({"token": tokens.get("access_token")})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        if token := request.session.get("token"):
            async with db_helper.session_factory() as session:
                try:
                    if user := await get_current_user(token, session):
                        if user.is_admin:
                            return True
                except HTTPException:
                    pass
        return False


authentication_backend = AdminAuth(secret_key="...")