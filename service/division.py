from utils.abstract_repository import AbstractRepository
from schemas.division import DivisionCreate
from schemas.division import DivisionUpdate


class DivisionService:
    def __init__(self, repository: AbstractRepository):
        self._repository: AbstractRepository = repository()  # type: ignore

    async def get_item_by_id(self, id: int):
        return await self._repository.get_by_id(id=id)

    async def get_all_item(self):
        return await self._repository.get_all()

    async def delete_item_by_id(self, id: int):
        return await self._repository.delete_by_id(id=id)

    async def update_item_by_id(self, id: int, data: DivisionUpdate):
        division_update = data.model_dump(exclude_unset=True)
        result = await self._repository.update_by_id(id=id, data=division_update)
        return result

    async def create_new_item(self, data: DivisionCreate):
        # print("_+_+_+_+_+_+_+_+_+_+_+_")
        division_create = data.model_dump()
        result = await self._repository.create_new(division_create)  # type: ignore
        return result
