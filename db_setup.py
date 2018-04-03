# Creates (or connects to) the database and adds tables and columns
import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    """Class for table named 'user'"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(80), nullable = False)
    picture = Column(String(250))

class Category(Base):
    """Class for table named 'category'"""
    __tablename__ = 'category'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("category", order_by=id))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

class Item(Base):
    """Class for table named 'item'"""
    __tablename__ = 'item'

    id = Column(Integer, primary_key = True)
    name = Column(String(80))
    dateadded = Column(Date)
    desc = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("item", order_by=id))
    cat_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", backref=backref("item", order_by=id))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'dateadded': self.dateadded,
            'desc': self.desc,
        }


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
