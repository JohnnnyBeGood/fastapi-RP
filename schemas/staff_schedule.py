from typing import Optional
from .core import CoreModel
from .core import IDModelMixin


class StaffScheduleBase(CoreModel):
    department_id: int
    division_id: int
    position_id: int
    comment: str
    is_vacancy: bool
    is_archival: bool


class StaffScheduleCreate(StaffScheduleBase):
    pass


class StaffScheduleInDB(IDModelMixin, StaffScheduleBase):
    pass


class StaffSchedulePublic(IDModelMixin, StaffScheduleBase):
    pass


class StaffScheduleUpdate(StaffScheduleBase):
    department_id: Optional[int] = None
    division_id: Optional[int] = None
    position_id: Optional[int] = None
    comment: Optional[str] = None
    is_vacancy: Optional[bool] = None
    is_archival: Optional[bool] = None
