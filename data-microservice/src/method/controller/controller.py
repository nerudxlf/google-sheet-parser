from datetime import datetime

from sqlalchemy import orm

from src.method.controller.a_controller import AController
from src.method.controller.i_controller import IController
from src.method.service.i_service import IService
from src.schemes.scheme_order import SchemeOrder


class Controller(IController, AController):
    @staticmethod
    async def update(message: dict, service: IService, db: orm.Session):
        current_values = message.get("data")[1:]
        for value in current_values:
            current_data = await service.get(value[0], db)
            tmp_order = SchemeOrder(
                data_id=value[0],
                order_num=value[1],
                price_dollar=value[2],
                price_rub=value[3],
                date=datetime.strptime(value[4], "%d.%m.%Y").date()
            )
            if not current_data:
                await service.add(tmp_order, db)
            elif current_data:
                from_orm = SchemeOrder.from_orm(current_data)
                if (not from_orm == tmp_order) and from_orm.data_id == tmp_order.data_id:
                    await service.update(value[0], tmp_order, db)

    @staticmethod
    async def delete(message: dict, service: IService, db: orm.Session):
        all_data = await service.get_all(db)
        current_values = message.get("data")[1:]
        current_values_scheme_order_set = set()
        all_data_scheme_order_set = set()
        for value in current_values:
            tmp_order = SchemeOrder(
                data_id=value[0],
                order_num=value[1],
                price_dollar=value[2],
                price_rub=value[3],
                date=datetime.strptime(value[4], "%d.%m.%Y").date()
            )
            current_values_scheme_order_set.add(tmp_order)
        for item in all_data:
            all_data_scheme_order_set.add(SchemeOrder.from_orm(item))
        result_set = all_data_scheme_order_set - current_values_scheme_order_set
        for item in result_set:
            await service.delete(item.data_id, db)
