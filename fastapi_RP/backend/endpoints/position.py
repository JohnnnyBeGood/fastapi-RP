from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List
from fastapi_RP.backend.service.position import PositionService
from fastapi_RP.backend.endpoints.dependencies import position_service
from fastapi_RP.backend.schemas.position import PositionInDB
from fastapi_RP.backend.schemas.position import PositionCreate
from fastapi_RP.backend.schemas.position import PositionUpdate
from fastapi_RP.backend.models.position import Position

router = APIRouter(tags=["Position Area"])

CommonsDep = Annotated[PositionService, Depends(position_service)]  # type: ignore


@router.get("/")
async def foo():
    return {"from Position"}


@router.get("/all", response_model=List[PositionInDB])
async def get_all(position_service: CommonsDep):
    result = await position_service.get_all_item()
    return result


@router.get("/{id}", response_model=PositionInDB)
async def get_item_by_id(id: int, position_service: CommonsDep):
    result = await position_service.get_item_by_id(id=id)
    return result


@router.post("/create", response_model=PositionInDB)
async def create_new(data: PositionCreate, position_service: CommonsDep):
    result = await position_service.create_new_item(data=data)
    return result


@router.put("/update/{id}", response_model=PositionUpdate)
async def update_item(id: int, data: PositionUpdate, position_service: CommonsDep):
    result = await position_service.update_item_by_id(id=id, data=data)
    return result


@router.delete("/delete/{id}")
async def delete_item(id: int, position_service: CommonsDep):
    result = await position_service.delete_item_by_id(id=id)
    return
