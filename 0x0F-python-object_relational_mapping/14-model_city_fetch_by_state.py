#!/usr/bin/python3
"""Print all city ojects"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        state = session.query(State).filter(
                State.id == city.state_id).one_or_none()
        if state:
            print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
