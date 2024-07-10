#!/usr/bin/python3
"""Deltes a state from the database"""

import sys
from sqlalchemy import create_engine
from slqalchemy.orm import sessionmaker
from model_state import Base, State


def delete_state(usname, pswrd, db_name):
    """deletes a state from the database"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:"
                           "3306/{}".format(usname, pswrd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    with_a = session.query(State).filter(State.name.like('%a%')).all()

    for a in with_a:
        session.delete(a)
    session.commit()


if __name__ == "__main__":
    delete_state(sys.argv[1], sys.argv[2], sys.argv[3])
