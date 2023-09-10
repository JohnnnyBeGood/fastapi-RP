from utils.sql_repository import SQLAbstractRepository
from models.department import Department


class DepartmentRepository(SQLAbstractRepository):
    model = Department

