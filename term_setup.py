### To run from terminal python prompt use these commands###
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item, User
engine = create_engine(''sqlite:///catalog.db'')
Base = declarative_base()
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
