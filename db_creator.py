#create database (only create database not connect to flask)
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
engine = create_engine('sqlite:///app_db.db', echo=True)#object engine to create database
Base = declarative_base()#base class of table

class AddUserData(Base):
    __tablename__ = "tbl_add_user_data"
    id = Column(Integer, primary_key=True)
    #username = Column(String)
    #password = Column(String)
    date = Column(String)
    age = Column(String)
    gender = Column(String)
    def __repr__(self):
        return "{}".format(self.name)
"""
class AddDish(Base):
    """"""
    __tablename__ = "tbl_add_dish"
    id = Column(Integer, primary_key=True)
    date = Column(String)
    name = Column(String)
    #pic = Column(String)
    calories = Column(Integer)
    carbohydrate = Column(Integer)
    protein = Column(Integer)
    #something_more = relationship("AddUserData", backref=backref(
        #"AddDish", order_by=id))
    #something_more = Column(String, ForeignKey("AddUserData.id"))
# create tables
"""
Base.metadata.create_all(engine)