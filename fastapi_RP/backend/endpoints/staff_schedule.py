from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List
from fastapi_RP.backend.service.staff_schedule import StaffScheduleService
from fastapi_RP.backend.endpoints.dependencies import staff_schedule_service
from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleInDB
from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleCreate
from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleUpdate
from fastapi_RP.backend.models.staff_schedule import StaffSchedule


router = APIRouter(tags=["Staff Schedule Area"])

CommonsDep = Annotated[StaffScheduleService, Depends(staff_schedule_service)]  # type: ignore


@router.get("/")
async def foo():
    return {"from Staff Schedule"}


@router.get("/all", response_model=List[StaffScheduleInDB])
async def get_all(staff_service: CommonsDep):
    result = await staff_service.get_all_item()
    return result


@router.get("/{id}", response_model=StaffScheduleInDB)
async def get_item_by_id(id: int, staff_service: CommonsDep):
    result = await staff_service.get_item_by_id(id=id)
    return result


@router.post("/create", response_model=StaffScheduleInDB)
async def create_new(data: StaffScheduleCreate, staff_service: CommonsDep):
    result = await staff_service.create_new_item(data=data)
    return result


@router.put("/update/{id}", response_model=StaffScheduleUpdate)
async def update_item(id: int, data: StaffScheduleUpdate, staff_service: CommonsDep):
    result = await staff_service.update_item_by_id(id=id, data=data)
    return result


@router.delete("/delete/{id}")
async def delete_item(id: int, staff_service: CommonsDep):
    result = await staff_service.delete_item_by_id(id=id)
    return
