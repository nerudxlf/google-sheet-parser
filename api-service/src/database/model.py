import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative


class Data(_declarative.declarative_base()):
    """
    Data table model
    """
    __tablename__: str = "data"
    data_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    order_num = _sql.Column(_sql.Integer, nullable=False)
    price_dollar = _sql.Column(_sql.String, nullable=False)
    price_rub = _sql.Column(_sql.String, nullable=False)
    date = _sql.Column(_sql.Date, nullable=False)
