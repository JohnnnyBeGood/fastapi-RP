from fastapi_RP.backend.utils.abstract_repository import AbstractRepository
from fastapi_RP.backend.schemas.department import DepartmentCreate
from fastapi_RP.backend.schemas.department import DepartmentUpdate


class DepartmentService:
    def __init__(self, repository: AbstractRepository):
        self._repository: AbstractRepository = repository()  # type: ignore

    # def __init__(self, repository: AbstractRepository):
    #     self.repository: AbstractRepository = repository()  # type: ignore

    async def get_item_by_id(self, id: int):
        return await self._repository.get_by_id(id=id)

    async def get_all_item(self):
        # departs=await self.
        return await self._repository.get_all()

    async def delete_item_by_id(self, id: int):
        return await self._repository.delete_by_id(id=id)

    async def update_item_by_id(self, id: int, data: DepartmentUpdate):
        depart_update = data.model_dump(exclude_unset=True)
        result = await self._repository.update_by_id(id=id, data=depart_update)
        return result

    async def create_new_item(self, data: DepartmentCreate):
        print("_+_+_+_+_+_+_+_+_+_+_+_")
        depart_create = data.model_dump()
        qq = await self._repository.create_new(depart_create)  # type: ignore

        return qq  # self._repository.create_new(data=depart_create)
