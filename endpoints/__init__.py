from fastapi import APIRouter
from .department import router as depart_router
from .division import router as division_router
from .position import router as position_router
from .staff_schedule import router as staff_schedule_router


api_router = APIRouter(prefix="/service")


api_router.include_router(depart_router, prefix="/department")
api_router.include_router(division_router, prefix="/division")
api_router.include_router(position_router, prefix="/position")
api_router.include_router(staff_schedule_router, prefix="/staff-schedule")
