from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.session import sessionmanager
from endpoints import api_router

# жёстко пропишем тип и путь к нашей БД
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///my_db.sqlite"


def init_app() -> FastAPI:
    sessionmanager.init(SQLALCHEMY_DATABASE_URL)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with sessionmanager.connect() as connect:
            await sessionmanager.create_all(connect)
        yield

    server = FastAPI(title="FastAPI Repository Example", lifespan=lifespan)  # type: ignore
    server.include_router(api_router)
    return server
