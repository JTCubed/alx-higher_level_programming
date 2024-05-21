#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def listsa(usname, passwrd, dbname):
    """lists all State objects that contain the letter a"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:'
                           '3306/{}'.format(usname, passwrd, dbname))

    Session = sessionmaker(bind=engine)
    session = Session()

    a = session.query(State.id, State.name).filter(State.name.like(
        '%a%')).all()
    for i, j in a:
        print("{}: {}".format(i, j))


if __name__ == '__main__':
    listsa(sys.argv[1], sys.argv[2], sys.argv[3])
