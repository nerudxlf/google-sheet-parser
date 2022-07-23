import datetime

import pydantic as _pydantic


class SchemeOrder(_pydantic.BaseModel):
    data_id: int
    order_num: int
    price_dollar: str
    price_rub: str
    date: datetime.date

    class Config:
        orm_mode = True

    def __key(self):
        return self.data_id, self.order_num, self.price_dollar, self.price_rub, self.date

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.__key() == other.__key()
        return NotImplemented

    def __hash__(self):
        return hash(self.__key())
