import fastapi_RP.backend.webapps

from typing import List
from typing import Optional
from typing import Annotated
from fastapi import APIRouter
from fastapi import Request
from fastapi import responses
from fastapi import Depends

from .from_staff_schedule import StaffScheduleCreateForm
from .from_staff_schedule import StaffScheduleEditForm


from fastapi_RP.backend.endpoints.dependencies import staff_schedule_service
from fastapi_RP.backend.endpoints.dependencies import staff_schedule_service_mixin
from fastapi_RP.backend.endpoints.dependencies import department_service
from fastapi_RP.backend.endpoints.dependencies import division_service
from fastapi_RP.backend.endpoints.dependencies import position_service


from fastapi_RP.backend.service.staff_schedule import StaffScheduleService
from fastapi_RP.backend.service.staff_schedule import StaffScheduleServiceMixin
from fastapi_RP.backend.service.department import DepartmentService
from fastapi_RP.backend.service.division import DivisionService
from fastapi_RP.backend.service.position import PositionService

from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleInDB
from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleCreate
from fastapi_RP.backend.schemas.staff_schedule import StaffScheduleUpdate

from sqlalchemy import text

router = APIRouter(include_in_schema=True)

CommonsDep = Annotated[StaffScheduleService, Depends(staff_schedule_service)]  # type: ignore
CommonsDepMixin = Annotated[
    StaffScheduleServiceMixin, Depends(staff_schedule_service_mixin)
]
CommonsDep_depart = Annotated[DepartmentService, Depends(department_service)]
CommonsDep_divis = Annotated[DivisionService, Depends(division_service)]
CommonsDep_posit = Annotated[PositionService, Depends(position_service)]


RAW_SQL = text(
    """SELECT tblStaffSchedule.id as id, tblDepartment.id as depart_id, tblDepartment.name as depart, 
        tblDivision.id as division_id, tblDivision.name as division, tblPosition.id as position_id, tblPosition.name as position,
        tblStaffSchedule.is_vacancy as is_vacancy, tblStaffSchedule.is_archival as is_archival,
        tblStaffSchedule.comment as comment
        from tblStaffSchedule, tblDepartment, tblDivision, tblPosition 
        WHERE tblDepartment.id=tblStaffSchedule.department_id and tblDivision.id=tblStaffSchedule.division_id and tblPosition.id=tblStaffSchedule.position_id
        ORDER by tblDepartment.id, tblDivision.id ASC"""
)


async def get_context():
    dep_service = department_service()
    div_service = division_service()
    pos_service = position_service()
    departs = await dep_service.get_all_item()
    division = await div_service.get_all_item()
    position = await pos_service.get_all_item()
    context = {
        "request": None,
        "depart": departs,
        "division": division,
        "position": position,
    }
    return context


@router.get("/full-staff-schedule", response_class=responses.HTMLResponse)
async def get_all_staff_records(
    request: Request, staff_schedule_service_mixin: CommonsDepMixin
):
    full_staff_schedule = await staff_schedule_service_mixin.get_all_items(RAW_SQL)
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "staff_schedule/staff_schedule_list.html",
        {"request": request, "full_staff_schedule": full_staff_schedule},
    )


@router.get("/create-a-staff-record", response_class=responses.HTMLResponse)
async def create_staffschedule_init(request: Request):
    context = await get_context()
    context["request"] = request
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "staff_schedule/create_staff_record.html", context=context
    )


@router.post("/create-a-staff-record", response_class=responses.HTMLResponse)
async def create_staffschedule_submit(
    request: Request, staff_schedule_service: CommonsDep
):
    form = StaffScheduleCreateForm(request)
    await form.load_data()

    if form.is_valid():
        try:
            #         # token = request.cookies.get("access_token")
            #         # scheme, param = get_authorization_scheme_param(
            #         #     token
            #         # )  # scheme will hold "Bearer" and param will hold actual token value
            #         # current_user: User = get_current_user_from_token(token=param, db=db)
            data = StaffScheduleCreate(**form.__dict__)
            staff_record = await staff_schedule_service.create_new_item(
                data=data
            )  # create_new_job(job=job, db=db, owner_id=current_user.id)
        #         # return responses.RedirectResponse(
        #         #     f"/details/{job.id}", status_code=status.HTTP_302_FOUND
        #         # )
        except Exception as e:
            print(e)
    #         form.__dict__.get("errors").append(
    #             "You might not be logged in, In case problem persists please contact us."
    #         )
    #         return fastapi_RP.backend.webapps.templates.TemplateResponse(
    #             "staff_schedule/create_staff_record.html", form.__dict__
    #         )
    return responses.RedirectResponse(
        "/staff-schedule/full-staff-schedule", status_code=303
    )
    # return templates.TemplateResponse(
    #     "department/create_department.html", form.__dict__
    # )

    # # depart = await staff_schedule_service.create_new_item(data=data)
    # return templates.TemplateResponse(
    #     "department/create_department.html", {"request": request, "depart": depart}
    # )


@router.get("/edit-staff-record/{id}", response_class=responses.HTMLResponse)
async def edit_staffschedule_init(
    request: Request, id: int, staff_schedule_service: CommonsDep
):
    context = await get_context()
    context["request"] = request
    staff_record = await staff_schedule_service.get_item_by_id(id=id)
    context["staff_record"] = staff_record
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "staff_schedule/edit_staff_record.html", context
    )


@router.post("/edit-staff-record/{id}", response_class=responses.HTMLResponse)
async def edit_staffschedule_submit(
    request: Request, id: int, staff_schedule_service: CommonsDep
):
    form = StaffScheduleEditForm(request=request)
    await form.load_data()
    data = StaffScheduleUpdate(**form.__dict__)
    result = await staff_schedule_service.update_item_by_id(id=id, data=data)
    return responses.RedirectResponse(
        "/staff-schedule/full-staff-schedule", status_code=303
    )


@router.get("/delete-depart/{id}", response_class=responses.HTMLResponse)
async def delete_stuff_record(
    request: Request, id: int, staff_schedule_service: CommonsDep
):
    result = await staff_schedule_service.delete_item_by_id(id=id)
    return responses.RedirectResponse(
        "/staff-schedule/full-staff-schedule", status_code=303
    )
