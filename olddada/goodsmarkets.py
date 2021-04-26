import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class GoodMarket(SqlAlchemyBase):
    __tablename__ = 'goodmarkets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    marketplaceid = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("marketplaces.id"))
    marketplace = orm.relation('MarketPlace')

    goodid = sqlalchemy.Column(sqlalchemy.Integer,
                                      sqlalchemy.ForeignKey("goods.id"))
    good = orm.relation('Good')
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
