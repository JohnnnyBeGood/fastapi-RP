import fastapi_RP.backend.webapps

from fastapi import APIRouter
from fastapi import Request
from fastapi import requests
from fastapi import Depends
from fastapi import responses

from typing import List
from typing import Annotated
from typing import Optional

from fastapi_RP.backend.schemas.division import DivisionCreate
from fastapi_RP.backend.schemas.division import DivisionUpdate

from fastapi_RP.backend.service.division import DivisionService
from fastapi_RP.backend.endpoints.dependencies import division_service

from .form_division import DivisionCreateForm
from .form_division import DivisionEditForm

router = APIRouter(include_in_schema=True)
CommonsDep = Annotated[DivisionService, Depends(division_service)]  # type: ignore


@router.get("/all-divisions", response_class=responses.HTMLResponse)
async def get_all_division(request: Request, division_service: CommonsDep):
    divisions = await division_service.get_all_item()
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "division/division_list.html", {"request": request, "divisions": divisions}
    )


@router.get("/create-a-division", response_class=responses.HTMLResponse)
async def create_division_init(request: Request, division_service: CommonsDep):
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "division/create_division.html", {"request": request}
    )


@router.post("/create-a-division", response_class=responses.HTMLResponse)
async def create_division_submit(request: Request, division_service: CommonsDep):
    form = DivisionCreateForm(request)
    await form.load_data()

    if form.is_valid():
        try:
            # token = request.cookies.get("access_token")
            # scheme, param = get_authorization_scheme_param(
            #     token
            # )  # scheme will hold "Bearer" and param will hold actual token value
            # current_user: User = get_current_user_from_token(token=param, db=db)
            data = DivisionCreate(**form.__dict__)
            division = await division_service.create_new_item(
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
                "department/create_division.html", form.__dict__
            )
    return responses.RedirectResponse("/division/all-divisions", status_code=303)
    # return templates.TemplateResponse(
    #     "department/create_department.html", form.__dict__
    # )

    # # depart = await department_service.create_new_item(data=data)
    # return templates.TemplateResponse(
    #     "department/create_department.html", {"request": request, "depart": depart}
    # )


@router.get("/edit-division/{id}", response_class=responses.HTMLResponse)
async def edit_division_init(request: Request, id: int, division_service: CommonsDep):
    division = await division_service.get_item_by_id(id=id)
    sel_my = [43, 76, 978, 234, 556]
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "division/edit_division.html",
        {"request": request, "division": division, "sel_my": sel_my},
    )


@router.post("/edit-division/{id}", response_class=responses.HTMLResponse)
async def edit_division_submit(request: Request, id: int, division_service: CommonsDep):
    form = DivisionEditForm(request=request)
    await form.load_data()
    data = DivisionUpdate(**form.__dict__)
    result = await division_service.update_item_by_id(id=id, data=data)
    return responses.RedirectResponse("/division/all-divisions", status_code=303)


@router.get("/delete-division/{id}", response_class=responses.HTMLResponse)
async def delete_division(request: Request, id: int, division_service: CommonsDep):
    result = await division_service.delete_item_by_id(id=id)
    return responses.RedirectResponse("/division/all-divisions", status_code=303)
