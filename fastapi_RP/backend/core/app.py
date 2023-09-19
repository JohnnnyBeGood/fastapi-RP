"""
docstring
"""
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi_RP.backend.core.session import sessionmanager
from fastapi_RP.backend.endpoints import api_router
from fastapi_RP.backend.webapps import webapp_router

# жёстко пропишем тип и путь к нашей БД
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///fastapi_RP/backend/my_db.sqlite"
BASE_PATH = Path(__file__).resolve().parents[2]
# templatest = Jinja2Templates(directory=str(BASE_PATH / "templates"))


def init_app() -> FastAPI:
    """
    docstring
    """
    sessionmanager.init(SQLALCHEMY_DATABASE_URL)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with sessionmanager.connect() as connect:
            await sessionmanager.create_all(connect)
        yield

    server = FastAPI(title="FastAPI Repository Example", lifespan=lifespan)  # type: ignore
    server.include_router(api_router)
    server.include_router(webapp_router)
    server.mount(
        "/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static"
    )
    return server
