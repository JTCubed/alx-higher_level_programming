#!/usr/bin/python3
"""selects first state from db"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


def selectstate(usname, passwrd, dbname):
    """selects first state from db"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:'
                           '3306/{}'.format(usname, passwrd, dbname))

    Session = sessionmaker(bind=engine)

    session = Session()
    first_state = session.query(State.id, State.name).first()
    print("{}: {}".format(first_state[0], first_state[1]))


if __name__ == '__main__':
    selectstate(sys.argv[1], sys.argv[2], sys.argv[3])
