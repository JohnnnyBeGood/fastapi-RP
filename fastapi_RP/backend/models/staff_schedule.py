# модель описывает "Штатное расписание" состоящее из
# Должность -> Отделение -> Отдел -> Штатное Расписание
from sqlalchemy import ForeignKey, String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from fastapi_RP.backend.models.base import Base
from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleInDB


class StaffSchedule(Base):
    __tablename__ = "tblStaffSchedule"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )
    is_vacancy: Mapped[bool] = mapped_column(Boolean, default=False)
    is_archival: Mapped[bool] = mapped_column(Boolean, default=False)
    comment: Mapped[str] = mapped_column(String)
    department_id: Mapped[int] = mapped_column(ForeignKey("tblDepartment.id"))
    division_id: Mapped[int] = mapped_column(ForeignKey("tblDivision.id"))
    position_id: Mapped[int] = mapped_column(ForeignKey("tblPosition.id"))

    def to_read_model(self) -> StaffScheduleInDB:
        return StaffScheduleInDB(
            id=self.id,
            is_vacancy=self.is_vacancy,
            is_archival=self.is_archival,
            comment=self.comment,
            department_id=self.department_id,
            division_id=self.division_id,
            position_id=self.position_id,
        )
