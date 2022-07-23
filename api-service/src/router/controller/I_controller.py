from sqlalchemy import orm

from src.router.service.i_service import IService


class IController:
    @staticmethod
    async def get(service: IService, db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def total(service: IService, db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def data_per_day(service: IService, db: orm.Session):
        raise NotImplementedError()