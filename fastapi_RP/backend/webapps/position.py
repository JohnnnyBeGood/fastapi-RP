import fastapi_RP.backend.webapps

from fastapi import APIRouter
from fastapi import Request
from fastapi import requests
from fastapi import Depends
from fastapi import responses

from typing import List
from typing import Annotated
from typing import Optional

from fastapi_RP.backend.schemas.position import PositionCreate
from fastapi_RP.backend.schemas.position import PositionUpdate

from fastapi_RP.backend.service.position import PositionService
from fastapi_RP.backend.endpoints.dependencies import position_service

from .form_position import PositionCreateForm
from .form_position import PositionEditForm


router = APIRouter(include_in_schema=True)
CommonsDep = Annotated[PositionService, Depends(position_service)]  # type: ignore


@router.get("/all-positions", response_class=responses.HTMLResponse)
async def get_all_position(request: Request, position_service: CommonsDep):
    positions = await position_service.get_all_item()
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "position/positions_list.html", {"request": request, "positions": positions}
    )


@router.get("/create-a-position", response_class=responses.HTMLResponse)
async def create_position_init(request: Request, position_service: CommonsDep):
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "position/create_position.html", {"request": request}
    )


@router.post("/create-a-position", response_class=responses.HTMLResponse)
async def create_position_submit(request: Request, position_service: CommonsDep):
    form = PositionCreateForm(request)
    await form.load_data()

    if form.is_valid():
        try:
            # token = request.cookies.get("access_token")
            # scheme, param = get_authorization_scheme_param(
            #     token
            # )  # scheme will hold "Bearer" and param will hold actual token value
            # current_user: User = get_current_user_from_token(token=param, db=db)
            data = PositionCreate(**form.__dict__)
            position = await position_service.create_new_item(
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
                "position/create_position.html", form.__dict__
            )
    return responses.RedirectResponse("/position/all-positions", status_code=303)
    # return templates.TemplateResponse(
    #     "department/create_department.html", form.__dict__
    # )

    # # depart = await department_service.create_new_item(data=data)
    # return templates.TemplateResponse(
    #     "department/create_department.html", {"request": request, "depart": depart}
    # )


@router.get("/edit-position/{id}", response_class=responses.HTMLResponse)
async def edit_position_init(request: Request, id: int, position_service: CommonsDep):
    position = await position_service.get_item_by_id(id=id)
    sel_my = [43, 76, 978, 234, 556]
    return fastapi_RP.backend.webapps.templates.TemplateResponse(
        "position/edit_position.html",
        {"request": request, "position": position, "sel_my": sel_my},
    )


@router.post("/edit-position/{id}", response_class=responses.HTMLResponse)
async def edit_position_submit(request: Request, id: int, position_service: CommonsDep):
    form = PositionEditForm(request=request)
    await form.load_data()
    data = PositionUpdate(**form.__dict__)
    result = await position_service.update_item_by_id(id=id, data=data)
    return responses.RedirectResponse("/position/all-positions", status_code=303)


@router.get("/delete-position/{id}", response_class=responses.HTMLResponse)
async def delete_position(request: Request, id: int, position_service: CommonsDep):
    result = await position_service.delete_item_by_id(id=id)
    return responses.RedirectResponse("/position/all-positions", status_code=303)
