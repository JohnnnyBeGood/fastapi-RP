from typing import Optional
from typing import Annotated
from pydantic import ConfigDict
from schemas.core import CoreModel
from schemas.core import IDModelMixin


class DepartmentBase(CoreModel):
    name: str
    sort_order: int


class DepartmentCreate(DepartmentBase):
    # name: str
    # sort_order: int
    pass


class DepartmentUpdate(DepartmentBase):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    sort_order: Optional[int] = None


class DepartmentInDB(IDModelMixin, DepartmentBase):
    model_config = ConfigDict(from_attributes=True)

    name: str
    sort_order: int


class DepartmentPublic(IDModelMixin, DepartmentBase):
    ...
