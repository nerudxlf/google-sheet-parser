from fastapi import APIRouter, Depends
from sqlalchemy import orm

from setttings_env import DB_ROOT, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from src.database.connect.db_factory import DB
from src.database.repositories.i_repo import IRepo
from src.router.controller.I_controller import IController
from src.router.controller.controller import Controller
from src.router.service.i_service import IService
from src.router.service.service import Service

router = APIRouter(
    prefix="/api",
    tags=["data"],
    responses={404: {"description": "Not found"}}
)

pg_db: IRepo = DB.postgres(DB_ROOT, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)


@router.get('/data/')
async def get_data(
        controller: IController = Depends(Controller),
        service: IService = Depends(Service),
        db: orm.Session = Depends(pg_db.connect)
):
    result = await controller.get(service, db)
    return result


@router.get('/total/')
async def get_total(
        controller: IController = Depends(Controller),
        service: IService = Depends(Service),
        db: orm.Session = Depends(pg_db.connect)
):
    result = await controller.total(service, db)
    return result


@router.get('/per_day/')
async def get_per_day(
        controller: IController = Depends(Controller),
        service: IService = Depends(Service),
        db: orm.Session = Depends(pg_db.connect)
):
    result = await controller.data_per_day(service, db)
    return result
