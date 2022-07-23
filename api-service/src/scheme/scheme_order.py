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
