# модель описывает должность сотрудника, которая есть в Отдлении, которое
# в свою очередь входит в Отдел
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base import Base
from schemas.position import PositionInDB
from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from models.staff_schedule import StaffSchedule


class Position(Base):
    __tablename__ = "tblPosition"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    name: Mapped[str] = mapped_column(String)
    count_position: Mapped[int] = mapped_column(Integer)
    sort_order: Mapped[int] = mapped_column(Integer)
    is_archive: Mapped[bool] = mapped_column(Boolean, default=False)
    staff_schedule: Mapped[List["StaffSchedule"]] = relationship()

    def to_read_model(self) -> PositionInDB:
        return PositionInDB(
            id=self.id,
            name=self.name,
            sort_order=self.sort_order,
            count_position=self.count_position,
            is_archive=self.is_archive,
        )
