from utils.sql_repository import SQLAbstractRepository
from models.division import Division


class DivisionRepository(SQLAbstractRepository):
    model = Division
