from fastapi_RP.backend.utils.sql_repository import SQLAbstractRepository
from fastapi_RP.backend.models.position import Position


class PositionRepository(SQLAbstractRepository):
    model = Position
