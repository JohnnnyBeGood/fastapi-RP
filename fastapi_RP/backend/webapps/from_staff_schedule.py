from typing import List
from typing import Optional

from fastapi import Request


class StaffScheduleCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.is_vacancy: Optional[str] = None
        self.is_archival: Optional[str] = None
        self.comment: Optional[int] = None
        self.department_id: Optional[str] = None
        self.division_id: Optional[str] = None
        self.position_id: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.is_vacancy = form.get("is_vacancy")
        self.is_archival = form.get("is_archival")
        self.comment = form.get("comment")
        self.department_id = form.get("department_id")
        self.division_id = form.get("division_id")
        self.position_id = form.get("position_id")

    def is_valid(self):
        if self.is_archival == None:
            self.is_archival = False
        if self.is_archival == "TRUE":
            self.is_archival = True
        if self.is_vacancy == None:
            self.is_vacancy = False
        if self.is_vacancy == "TRUE":
            self.is_vacancy = True
        if not self.errors:
            return True
        return False


class StaffScheduleEditForm:
    def __init__(self, request: Request) -> None:
        self.request = request
        self.errors: List = []
        self.is_vacancy: Optional[str] = None
        self.is_archival: Optional[str] = None
        self.comment: Optional[str] = None
        self.department_id: Optional[str] = None
        self.division_id: Optional[str] = None
        self.position_id: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.comment = form.get("comment")
        self.department_id = form.get("department_id")
        self.division_id = form.get("division_id")
        self.position_id = form.get("position_id")
        self.is_vacancy = form.get("is_vacancy")
        self.is_archival = form.get("is_archival")
        if self.is_archival == None:
            self.is_archival = False
        if self.is_archival == "TRUE":
            self.is_archival = True
        if self.is_vacancy == None:
            self.is_vacancy = False
        if self.is_vacancy == "TRUE":
            self.is_vacancy = True
