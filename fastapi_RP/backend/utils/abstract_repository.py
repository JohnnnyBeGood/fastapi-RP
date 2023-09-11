from abc import ABC
from abc import abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def create_new(self, data):
        return NotImplementedError

    @abstractmethod
    async def get_by_id(self, id: int):
        return NotImplementedError

    @abstractmethod
    async def get_all(self):
        return NotImplementedError

    @abstractmethod
    async def update_by_id(self, id, data):
        return NotImplementedError

    @abstractmethod
    async def delete_by_id(self, id: int):
        return NotImplementedError
