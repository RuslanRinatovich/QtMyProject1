import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Good(SqlAlchemyBase):
    __tablename__ = 'goods'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    goodtypeid = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("goods.id"))
    goodname = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    good = orm.relation('Good')