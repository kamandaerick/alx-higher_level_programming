#!/usr/bin/python3
"""Print the first state in the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    pattern = '%a%'
    states = session.query(State).filter(State.name.like(pattern)).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
