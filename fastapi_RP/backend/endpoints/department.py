from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List
from fastapi_RP.backend.service.department import DepartmentService
from fastapi_RP.backend.endpoints.dependencies import department_service
from fastapi_RP.backend.schemas.department import DepartmentInDB
from fastapi_RP.backend.schemas.department import DepartmentCreate
from fastapi_RP.backend.schemas.department import DepartmentUpdate

router = APIRouter(tags=["Department Area"])

CommonsDep = Annotated[DepartmentService, Depends(department_service)]  # type: ignore


@router.get("/")
async def foo():
    return {"from Department"}


@router.get("/all", response_model=List[DepartmentInDB])
async def get_all(department_service: CommonsDep):
    result = await department_service.get_all_item()
    return result


@router.get("/{id}", response_model=DepartmentInDB)
async def get_item_by_id(id: int, department_service: CommonsDep):
    result = await department_service.get_item_by_id(id=id)
    return result


@router.post("/create", response_model=DepartmentInDB)
async def create_new(
    data: DepartmentCreate,
    department_service: Annotated[DepartmentService, Depends(department_service)],
):
    result = await department_service.create_new_item(data=data)
    return result


@router.put("/update/{id}", response_model=DepartmentUpdate)
async def update_item(id: int, data: DepartmentUpdate, department_service: CommonsDep):
    result = await department_service.update_item_by_id(id=id, data=data)
    return result


@router.delete("/delete/{id}")
async def delete_item(id: int, department_service: CommonsDep):
    result = await department_service.delete_item_by_id(id=id)
    return
