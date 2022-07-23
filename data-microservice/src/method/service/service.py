from datetime import datetime

from sqlalchemy import orm

from src.database.model import Data
from src.method.service.a_service import AService
from src.method.service.i_service import IService
from src.schemes.scheme_order import SchemeOrder


class Service(IService, AService):
    @staticmethod
    async def get_all(db: orm.Session):
        data = db.query(Data).all()
        return data

    @staticmethod
    async def get(id: int, db: orm.Session):
        data = db.query(Data).filter(Data.data_id == id).first()
        return data

    @staticmethod
    async def delete(id: int, db: orm.Session):
        data = db.query(Data).filter(Data.data_id == id).first()
        db.delete(data)
        db.commit()

    @staticmethod
    async def update(id: int, attr: SchemeOrder, db: orm.Session):
        data = db.query(Data).filter(Data.data_id == id).first()
        for key, value in attr.dict().items():
            if value:
                setattr(data, key, value)
        db.commit()
        db.refresh(data)

    @staticmethod
    async def add(attr: SchemeOrder, db: orm.Session):
        data = Data(
            data_id=int(attr.data_id),
            order_num=int(attr.order_num),
            price_dollar=str(attr.price_dollar),
            price_rub=str(attr.price_rub),
            date=attr.date
        )
        db.add(data)
        db.commit()
        db.refresh(data)
