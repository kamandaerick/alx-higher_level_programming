#!/usr/bin/python3
'''Change the name of a state from the database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).one_or_none()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
