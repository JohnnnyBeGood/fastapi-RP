from sqlalchemy import insert, select, update, delete
from fastapi_RP.backend.utils.abstract_repository import AbstractRepository
from fastapi_RP.backend.core.session import get_db


class SQLAbstractRepository(AbstractRepository):
    model = None

    async def create_new(self, data):
        _session = await anext(get_db())  # type: ignore
        stmt = insert(self.model).values(**data).returning(self.model)  # type: ignore
        result = await _session.execute(stmt)
        await _session.commit()
        # await _session.refresh(result)
        return result.scalar_one_or_none()

    async def get_by_id(self, id: int):
        _session = await anext(get_db())  # type: ignore
        stmt = select(self.model).where(self.model.id == id)
        result = await _session.execute(stmt)
        await _session.commit()
        return result.scalar_one_or_none()

    async def get_all(self):
        _session = await anext(get_db())  # type: ignore
        stmt = select(self.model)
        result = await _session.execute(stmt)
        result = [row[0].to_read_model() for row in result.all()]
        return result

    async def update_by_id(self, id, data):
        _session = await anext(get_db())  # type: ignore
        stmt = update(self.model).where(self.model.id == id).values(data)
        result = await _session.execute(stmt)
        await _session.commit()
        stmt = select(self.model).where(self.model.id == id)
        result = await _session.execute(stmt)
        await _session.commit()
        return result.scalar_one_or_none()

    async def delete_by_id(self, id: int):
        _session = await anext(get_db())  # type: ignore
        stmt = delete(self.model).where(self.model.id == id)
        result = await _session.execute(stmt)
        await _session.commit()
        return {"success"}
