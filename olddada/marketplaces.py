import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class MarketPlace(SqlAlchemyBase):
    __tablename__ = 'marketplaces'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    marketid = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("markets.id"))
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    latitude = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    longitude = sqlalchemy.Column(sqlalchemy.Float, nullable=True)

    market = orm.relation('Market')

    goodmarkets = orm.relation("GoodMarkets", back_populates='goodmarket')
