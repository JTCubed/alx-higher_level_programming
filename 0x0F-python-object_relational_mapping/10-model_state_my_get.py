#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def namep(usname, passwrd, dbname, searchn):
    """prints the State object with the name passed as argument"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:'
                           '3306/{}'.format(usname, passwrd, dbname))

    Session = sessionmaker(bind=engine)
    session = Session()

    searchq = "%{}%".format(searchn)
    sta = session.query(State.id, State.name).filter(State.name.like(
        searchq)).first()

    if sta:
        if searchn in sta:
            print(sta[0])
    else:
        print('Not found')


if __name__ == '__main__':
    namep(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
