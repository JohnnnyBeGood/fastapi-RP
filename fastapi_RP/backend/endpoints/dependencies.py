from fastapi_RP.backend.repositiories.department import DepartmentRepository
from fastapi_RP.backend.repositiories.division import DivisionRepository
from fastapi_RP.backend.repositiories.position import PositionRepository
from fastapi_RP.backend.repositiories.staff_schedule import StaffScheduleRepository
from fastapi_RP.backend.repositiories.staff_schedule import StaffScheduleRepositoryMixin

from fastapi_RP.backend.service.department import DepartmentService
from fastapi_RP.backend.service.division import DivisionService
from fastapi_RP.backend.service.position import PositionService
from fastapi_RP.backend.service.staff_schedule import StaffScheduleService
from fastapi_RP.backend.service.staff_schedule import StaffScheduleServiceMixin


def department_service():
    return DepartmentService(DepartmentRepository)  # type: ignore


def division_service():
    return DivisionService(DivisionRepository)  # type: ignore


def position_service():
    return PositionService(PositionRepository)  # type: ignore


def staff_schedule_service():
    return StaffScheduleService(StaffScheduleRepository)  # type: ignore


def staff_schedule_service_mixin():
    return StaffScheduleServiceMixin(StaffScheduleRepositoryMixin)
