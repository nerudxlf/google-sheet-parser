from sqlalchemy import orm

from src.router.controller.I_controller import IController
from src.router.controller.a_crontroller import AController
from src.router.service.i_service import IService


class Controller(IController, AController):
    """Controller for processing request"""

    @staticmethod
    async def get(service: IService, db: orm.Session):
        result = await service.get_all(db)
        return result

    @staticmethod
    async def total(service: IService, db: orm.Session):
        data_total = await service.get_total(db)
        return sum([int(i[0]) for i in data_total])

    @staticmethod
    async def data_per_day(service: IService, db: orm.Session):
        data = await service.get_data_per_day(db)
        result = []
        for item in data:
            result.append({"name": item[0], "value": item[1]})
        return result
