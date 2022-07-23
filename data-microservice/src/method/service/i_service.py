from sqlalchemy import orm

from src.schemes.scheme_order import SchemeOrder


class IService:
    @staticmethod
    async def get_all(db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def get(id: int, db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def update(id: int, attr: SchemeOrder, db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def delete(id: int, db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def add(attr: SchemeOrder, db: orm.Session):
        raise NotImplementedError()
