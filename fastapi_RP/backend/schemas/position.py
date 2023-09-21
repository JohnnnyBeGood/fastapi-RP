from pydantic import ConfigDict
from typing import Optional
from fastapi_RP.backend.schemas.core import CoreModel
from fastapi_RP.backend.schemas.core import IDModelMixin


class PositionBase(CoreModel):
    name: Optional[str]
    count_position: Optional[int]
    sort_order: Optional[int]
    is_archive: Optional[bool]


class PositionCreate(PositionBase):
    name: str
    count_position: int
    sort_order: int
    is_archive: bool


class PositionInDB(IDModelMixin, PositionBase):
    model_config = ConfigDict(from_attributes=True)

    name: str
    count_position: int
    sort_order: int
    is_archive: bool


class PositionPublic(IDModelMixin, PositionBase):
    ...


class PositionUpdate(PositionBase):
    name: Optional[str]
    count_position: Optional[int]
    sort_order: Optional[int]
    is_archive: Optional[bool]
