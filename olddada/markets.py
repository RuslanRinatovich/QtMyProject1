import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class Market(SqlAlchemyBase):
    __tablename__ = 'markets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, unique=True, autoincrement=True)
    marketname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    logo = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    marketplaces = orm.relation('MarketPlaces', back_populates='market')