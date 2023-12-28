#!/usr/bin/python3
"""This script defines a class States that inherits from
the Base class
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class States(Base):
    """Definition of the State class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
