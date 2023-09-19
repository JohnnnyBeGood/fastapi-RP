from typing import List
from typing import Optional

from fastapi import Request


class DepartmentCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.sort_order: Optional[int] = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.sort_order = form.get("sort_order")

    def is_valid(self):
        if not self.name or not len(self.name) >= 2:
            self.errors.append("Укажите правльное название Отдела")
        # if not int(self.sort_order) or not int(self.sort_order) < 0:
        #     self.errors.append("код сортировки должен быть больше ноля")
        if not self.errors:
            return True
        return False


class DepartmentEditForm:
    def __init__(self, request: Request) -> None:
        self.request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.sort_order: Optional[int] = None
        self.select = None

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.sort_order = form.get("sort_order")
        self.select = form.get("select")
