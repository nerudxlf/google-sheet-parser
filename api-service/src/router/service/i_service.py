from sqlalchemy import orm


class IService:
    @staticmethod
    async def get_all(db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def get_total(db: orm.Session):
        raise NotImplementedError()

    @staticmethod
    async def get_data_per_day(db: orm.Session):
        raise NotImplementedError()