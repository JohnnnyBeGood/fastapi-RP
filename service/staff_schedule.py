from utils.abstract_repository import AbstractRepository
from schemas.staff_schedule import StaffScheduleCreate
from schemas.staff_schedule import StaffScheduleUpdate


class StaffScheduleService:
    def __init__(self, repository: AbstractRepository):
        self._repository: AbstractRepository = repository()  # type: ignore

    async def get_item_by_id(self, id: int):
        return await self._repository.get_by_id(id=id)

    async def get_all_item(self):
        return await self._repository.get_all()

    async def delete_item_by_id(self, id: int):
        return await self._repository.delete_by_id(id=id)

    async def update_item_by_id(self, id: int, data: StaffScheduleUpdate):
        staff_update = data.model_dump(exclude_unset=True)
        result = await self._repository.update_by_id(id=id, data=staff_update)
        return result

    async def create_new_item(self, data: StaffScheduleCreate):
        # print("_+_+_+_+_+_+_+_+_+_+_+_")
        staff_create = data.model_dump()
        result = await self._repository.create_new(staff_create)  # type: ignore
        return result
