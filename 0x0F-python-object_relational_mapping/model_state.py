#!/usr/bin/python3
'''Define class State and an instance Base'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
'''Define class State inheriting from BAse'''
class State(Base):
    '''State class
    Attributes:
    __tablename__ (str): Name of the table
    id (int): Primary key (state id)
    name (str): Name of the state
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
