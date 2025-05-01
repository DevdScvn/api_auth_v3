import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from admin_panel.auth import authentication_backend
from admin_panel.user import UserAdmin
from database import db_helper
from settings.config import settings

from users.router import router as users_router
from auth.router import router as auth_router

log = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    log.warning("dispose_engine")
    await db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan,
)

main_app.include_router(users_router)
main_app.include_router(auth_router)

admin = Admin(
    main_app, engine=db_helper.engine, authentication_backend=authentication_backend
)

admin.add_view(UserAdmin)

if __name__ == "__main__":
    uvicorn.run("main:main_app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)