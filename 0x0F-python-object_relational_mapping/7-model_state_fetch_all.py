#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def liststates(usname, pswrd, name):

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(usname, pswrd, name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    sstates = session.query(State).order_by(State.id).all()
    for instance in sstates:
        print(instance.id, end='')
        print(": " + instance.name)


if __name__ == '__main__':
    liststates(sys.argv[1], sys.argv[2], sys.argv[3])
