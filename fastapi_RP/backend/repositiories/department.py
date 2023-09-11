from fastapi_RP.backend.utils.sql_repository import SQLAbstractRepository
from fastapi_RP.backend.models.department import Department


class DepartmentRepository(SQLAbstractRepository):
    model = Department
