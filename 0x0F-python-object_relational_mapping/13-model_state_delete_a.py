#!/usr/bin/python3
'''Deletes all State obects with a name containing letter a'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State).filter(State.name.like('%a%')).all()
    for state in a_states:
        session.delete(state)

    session.commit()
    session.close()
