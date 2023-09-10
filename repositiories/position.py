from utils.sql_repository import SQLAbstractRepository
from models.position import Position


class PositionRepository(SQLAbstractRepository):
    model = Position
