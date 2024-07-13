import sqlalchemy
from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'
    user_id = sqlalchemy.Column(sqlalchemy.String,
                           primary_key=True)
    join_datetime = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    income = sqlalchemy.Column(sqlalchemy.Float)
    kids = sqlalchemy.Column(sqlalchemy.Integer)
    teenagers = sqlalchemy.Column(sqlalchemy.Integer)
    marital = sqlalchemy.Column(sqlalchemy.String)
    education = sqlalchemy.Column(sqlalchemy.String)
