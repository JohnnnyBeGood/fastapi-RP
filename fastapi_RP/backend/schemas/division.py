from pydantic import ConfigDict
from typing import Optional
from fastapi_RP.backend.schemas.core import CoreModel
from fastapi_RP.backend.schemas.core import IDModelMixin


class DivisionBase(CoreModel):
    name: str
    sort_order: int


class DivisionCreate(DivisionBase):
    pass


class DivisionInDB(IDModelMixin, DivisionBase):
    model_config = ConfigDict(from_attributes=True)

    name: str
    sort_order: int


class DivisionPublic(IDModelMixin, DivisionBase):
    ...


class DivisionUpdate(DivisionBase):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    sort_order: Optional[int] = None