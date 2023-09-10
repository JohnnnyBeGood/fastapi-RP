from utils.sql_repository import SQLAbstractRepository
from models.staff_schedule import StaffSchedule


class StaffScheduleRepository(SQLAbstractRepository):
    model = StaffSchedule
