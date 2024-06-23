#!/usr/bin/python3
"""Define class City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class City

    Args:
        Base (class): The base class for the table
        id (int): The id of the table
        name (str): The name of the table
        state_id (int): The id of the state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
