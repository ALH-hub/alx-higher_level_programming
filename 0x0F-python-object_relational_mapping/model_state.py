#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represent a state for database

    __tablename__ (str): name of table
    id (sqlalchemy.Integer): state's id
    name (sqlalchemy.String): state's name
    """
    __tablename__ = "states"
    id = Column(sqlalchemy.Integer, primary_key=True, unique=True, nullable=False)
    name = Column(sqlalchemy.String(128), nullable=False)
