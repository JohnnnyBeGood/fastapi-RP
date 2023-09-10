# модель описывает "Отделение", которое входит в "Отдел"
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from models.base import Base
from schemas.division import DivisionInDB
from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from models.staff_schedule import StaffSchedule


class Division(Base):
    __tablename__ = "tblDivision"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    name: Mapped[str] = mapped_column(String)
    sort_order: Mapped[int] = mapped_column(Integer)
    staff_schedule: Mapped[List["StaffSchedule"]] = relationship()

    def to_read_model(self) -> DivisionInDB:
        return DivisionInDB(
            id=self.id,
            name=self.name,
            sort_order=self.sort_order,
        )
