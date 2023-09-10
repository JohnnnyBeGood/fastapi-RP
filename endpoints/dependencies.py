from repositiories.department import DepartmentRepository
from repositiories.division import DivisionRepository
from repositiories.position import PositionRepository
from repositiories.staff_schedule import StaffScheduleRepository
from service.department import DepartmentService
from service.division import DivisionService
from service.position import PositionService
from service.staff_schedule import StaffScheduleService


def department_service():
    return DepartmentService(DepartmentRepository)  # type: ignore


def division_service():
    return DivisionService(DivisionRepository)


def position_service():
    return PositionService(PositionRepository)


def staff_schedule_service():
    return StaffScheduleService(StaffScheduleRepository)
