from pathlib import Path
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from .department import router as depart_router
from .division import router as division_router
from .position import router as position_router
from .staff_schedule import router as staff_router


webapp_router = APIRouter(include_in_schema=True)

webapp_router.include_router(depart_router, prefix="", tags=["Web Department"])
webapp_router.include_router(division_router, prefix="", tags=["Web Division"])
webapp_router.include_router(position_router, prefix="", tags=["Web Position"])
webapp_router.include_router(staff_router, prefix="", tags=["Web StaffSchedule"])

# BASE_PATH = Path(__file__).resolve().parents[2]
# templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
