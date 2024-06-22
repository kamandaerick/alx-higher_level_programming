#!/usr/bin/python3
'''Define class State and an instance Base'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
'''Define class State inheriting from BAse'''
class State(Base):
    '''
    __tablename__ (str): Name of the table
    id (int): Primary key (state id)
    name (str): Name of the state
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
