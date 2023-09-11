from fastapi_RP.backend.utils.sql_repository import SQLAbstractRepository
from fastapi_RP.backend.models.staff_schedule import StaffSchedule


class StaffScheduleRepository(SQLAbstractRepository):
    model = StaffSchedule
