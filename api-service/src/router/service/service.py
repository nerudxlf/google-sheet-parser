import sqlalchemy as _sql
from sqlalchemy import orm, cast

from src.database.model import Data
from src.router.service.a_service import AService
from src.router.service.i_service import IService


class Service(IService, AService):
    """
    Database query service
    """

    @staticmethod
    async def get_all(db: orm.Session):
        """
        Get all data from table Data
        :param db: Current session with database
        :return:
        """
        return db.query(Data).all()

    @staticmethod
    async def get_total(db: orm.Session):
        """
        Get total by price dollar
        :param db: Current session with database
        :return:
        """
        return db.query(Data.price_dollar).all()

    @staticmethod
    async def get_data_per_day(db: orm.Session):
        """
        Get data by day
        :param db: Current session with database
        :return:
        """
        return db.query(Data.date, _sql.func.sum(cast(Data.price_dollar, _sql.Integer))).group_by(Data.date).all()
