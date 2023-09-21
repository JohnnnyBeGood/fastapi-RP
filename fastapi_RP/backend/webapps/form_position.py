from typing import List
from typing import Optional

from fastapi import Request


class PositionCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.count_position: Optional[int] = None
        self.sort_order: Optional[int] = None
        self.is_archive: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.count_position = form.get("count_position")
        self.sort_order = form.get("sort_order")
        self.is_archive = form.get("is_archive")

    def is_valid(self):
        if not self.name or not len(self.name) >= 2:
            self.errors.append("Должность не может быть меньше 2х символов")
        if not int(self.sort_order) or int(self.sort_order) < 0:
            self.errors.append("код сортировки должен быть цифрой и больше ноля")
        if self.is_archive == None:
            self.is_archive = False
        if self.is_archive == "TRUE":
            self.is_archive = True
        if not self.errors:
            return True
        return False


class PositionEditForm:
    def __init__(self, request: Request) -> None:
        self.request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.sort_order: Optional[int] = None
        self.count_position: Optional[int] = None
        self.is_archive: Optional[bool] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.sort_order = form.get("sort_order")
        self.count_position = form.get("count_position")
        self.is_archive = form.get("is_archive")
