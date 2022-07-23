from fastapi import Depends, APIRouter, Response, Request
from jsonrpcserver import method, Success, Result, async_dispatch
from sqlalchemy import orm

from settings_env import DB_ROOT, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT
from src.database.connect.db_factory import DB
from src.database.repositories.i_repo import IRepo
from src.method.controller.controller import Controller
from src.method.controller.i_controller import IController
from src.method.service.i_service import IService
from src.method.service.service import Service

router = APIRouter(
    prefix="/api/v1",
    tags=["data"],
    responses={404: {"description": "Not found"}}
)

pg_db: IRepo = DB.postgres(DB_ROOT, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)


@method
async def data(context: tuple[IController, IService, orm.Session], message: dict) -> Result:
    """
    Method for working with json-rpc
    :param context:
    :param message:
    :return:
    """
    controller, service, db = context
    await controller.update(message, service, db)
    await controller.delete(message, service, db)
    return Success()


@router.post("/")
async def index(
        request: Request,
        current_controller: IController = Depends(Controller),
        db: orm.Session = Depends(pg_db.connect),
        current_service: IService = Depends(Service)
):
    return Response(await async_dispatch(await request.body(), context=(current_controller, current_service, db)))
