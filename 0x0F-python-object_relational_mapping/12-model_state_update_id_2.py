#!/usr/bin/python3
"""Update a record in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(usname, pswrd, db_name):
    """Update a record in the database"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:"
                           "3306/{}".format(usname, pswrd, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_n = session.query(State).filter_by(id=2).first()
    state_n.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    update_state(sys.argv[1], sys.argv[2], sys.argv[3])
