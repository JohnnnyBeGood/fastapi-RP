from fastapi_RP.backend.utils.sql_repository import SQLAbstractRepository
from fastapi_RP.backend.models.division import Division


class DivisionRepository(SQLAbstractRepository):
    model = Division
