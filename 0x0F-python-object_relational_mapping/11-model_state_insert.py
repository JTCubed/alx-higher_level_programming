#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

"""adding new state to the database"""

def new_state(usname, pswrd, db_name):
    """adding new state to the database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:'
                           '3306/{}'.format(usname, pswrd, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    Louisiana_state = State(name="Louisiana")
    session.add(Louisiana_state)
    new_sta = session.query(State).filter_by(name="Louisiana").first()
    print(new_sta.id)
    session.commit()


if __name__ == "__main__":
    new_state(sys.argv[1], sys.argv[2], sys.argv[3])
