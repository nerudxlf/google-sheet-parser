from sqlalchemy import orm

from src.method.service.i_service import IService


class IController:
    @staticmethod
    async def update(message: dict, service: IService, db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def delete(message: dict, service: IService, db: orm.Session):
        raise NotImplementedError()
