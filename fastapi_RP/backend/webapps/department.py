# from pathlib import Path
from typing import List
from typing import Optional
from typing import Annotated
from fastapi import APIRouter
from fastapi import Request
from fastapi import responses
from fastapi import Depends

from .form_department import DepartmentCreateForm
from .form_department import DepartmentEditForm


from fastapi_RP.backend.service.department import DepartmentService
from fastapi_RP.backend.endpoints.dependencies import department_service
from fastapi_RP.backend.schemas.department import DepartmentInDB
from fastapi_RP.backend.schemas.department import DepartmentCreate
from fastapi_RP.backend.schemas.department import DepartmentUpdate

import fastapi_RP.backend.webapps

# BASE_PATH = Path(__file__).resolve().parents[2]
# templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))


router = APIRouter(include_in_schema=True)
CommonsDep = Annotated[DepartmentService, Depends(department_service)]  # type: ignore


# @router.get("/", response_class=responses.HTMLResponse)
# async def home(request: Request):  # , db: Session = Depends(get_db), msg: str = None):
#     return fastapi_RP.backend.webapps.templates.TemplateResponse(
#         "general_pages/homepage.html", {"request": request}
#     )


@router.get("/all-departs", response_class=responses.HTMLResponse)
async def get_all_department(request: Request, department_service: CommonsDep):
    departs = await department_service.get_all_item()
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "department/departments_list.html", {"request": request, "departs": departs}
    )


@router.get("/create-a-depart", response_class=responses.HTMLResponse)
async def create_department_init(request: Request, department_service: CommonsDep):
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "department/create_department.html", {"request": request}
    )


@router.post("/create-a-depart", response_class=responses.HTMLResponse)
async def create_department_submit(request: Request, department_service: CommonsDep):
    form = DepartmentCreateForm(request)
    await form.load_data()

    if form.is_valid():
        try:
            # token = request.cookies.get("access_token")
            # scheme, param = get_authorization_scheme_param(
            #     token
            # )  # scheme will hold "Bearer" and param will hold actual token value
            # current_user: User = get_current_user_from_token(token=param, db=db)
            data = DepartmentCreate(**form.__dict__)
            depart = await department_service.create_new_item(
                data=data
            )  # create_new_job(job=job, db=db, owner_id=current_user.id)
            # return responses.RedirectResponse(
            #     f"/details/{job.id}", status_code=status.HTTP_302_FOUND
            # )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return fastapi_RP.backend.webapps.templates.TemplateResponse(
                "department/create_department.html", form.__dict__
            )
    return responses.RedirectResponse("/department/all-departs", status_code=303)
    # return templates.TemplateResponse(
    #     "department/create_department.html", form.__dict__
    # )

    # # depart = await department_service.create_new_item(data=data)
    # return templates.TemplateResponse(
    #     "department/create_department.html", {"request": request, "depart": depart}
    # )


@router.get("/edit-depart/{id}", response_class=responses.HTMLResponse)
async def edit_department_init(
    request: Request, id: int, department_service: CommonsDep
):
    depart = await department_service.get_item_by_id(id=id)
    sel_my = [43, 76, 978, 234, 556]
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "department/edit_department.html",
        {"request": request, "depart": depart, "sel_my": sel_my},
    )


@router.post("/edit-depart/{id}", response_class=responses.HTMLResponse)
async def edit_department_submit(
    request: Request, id: int, department_service: CommonsDep
):
    form = DepartmentEditForm(request=request)
    await form.load_data()
    data = DepartmentUpdate(**form.__dict__)
    result = await department_service.update_item_by_id(id=id, data=data)
    return responses.RedirectResponse("/department/all-departs", status_code=303)


@router.get("/delete-depart/{id}", response_class=responses.HTMLResponse)
async def delete_department(request: Request, id: int, department_service: CommonsDep):
    result = await department_service.delete_item_by_id(id=id)
    return responses.RedirectResponse("/department/all-departs", status_code=303)
