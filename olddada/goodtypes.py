import sqlalchemy
from sqlalchemy import orm


from .db_session import SqlAlchemyBase


class GoodType(SqlAlchemyBase):
    __tablename__ = 'goodtypes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    goodtypename = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    goods = orm.relation("Goods", back_populates='good')
