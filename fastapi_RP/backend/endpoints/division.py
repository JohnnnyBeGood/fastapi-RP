from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List
from fastapi_RP.backend.service.division import DivisionService
from fastapi_RP.backend.endpoints.dependencies import division_service
from fastapi_RP.backend.schemas.division import DivisionInDB
from fastapi_RP.backend.schemas.division import DivisionCreate
from fastapi_RP.backend.schemas.division import DivisionUpdate
from fastapi_RP.backend.models.division import Division

router = APIRouter(tags=["Division Area"])

CommonsDep = Annotated[DivisionService, Depends(division_service)]  # type: ignore


@router.get("/")
async def foo():
    return {"from Division"}


@router.get("/all", response_model=List[DivisionInDB])
async def get_all(division_service: CommonsDep):
    result = await division_service.get_all_item()
    return result


@router.get("/{id}", response_model=DivisionInDB)
async def get_item_by_id(id: int, division_service: CommonsDep):
    result = await division_service.get_item_by_id(id=id)
    return result


@router.post("/create", response_model=DivisionInDB)
async def create_new(data: DivisionCreate, division_service: CommonsDep):
    result = await division_service.create_new_item(data=data)
    return result


@router.put("/update/{id}", response_model=DivisionUpdate)
async def update_item(id: int, data: DivisionUpdate, division_service: CommonsDep):
    result = await division_service.update_item_by_id(id=id, data=data)
    return result


@router.delete("/delete/{id}")
async def delete_item(id: int, division_service: CommonsDep):
    result = await division_service.delete_item_by_id(id=id)
    return
