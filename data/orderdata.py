import sqlalchemy as sql
from sqlalchemy import orm
from db_session import SqlAlchemyBase



class Orderdata(SqlAlchemyBase):
    __tablename__ = "orderdata"
    userid = sql.Column(sql.String, sql.ForeignKey("users.userid"), primary_key=True)
    category = sql.Column(sql.String)
    avg_bill = sql.Column(sql.Float)
    id = orm.relationship("userdata")