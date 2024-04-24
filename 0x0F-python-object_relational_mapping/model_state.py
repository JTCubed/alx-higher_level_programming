#!/usr/bin/python3

"""Class repr a state"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """creates state table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
