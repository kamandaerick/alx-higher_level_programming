#!/usr/bin/python3
"""This script lists all states in a database"""
import MySQLdb
import sys


def select_states(username, password, db_name, state_name):
    """This function lists all states

    Args:
        username (string): username
        password (string): password
        db_name (string): database name
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cursor = db.cursor()
        query = (
          "SELECT * "
          "FROM states "
          "WHERE name=%s "
          "ORDER BY states.id ASC"
          )
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()

        for state in states:
            state_id, state_name = state[0], state[1]
            print(f"({state_id}, '{state_name}')")

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if 'db' in locals() and db.open:
            cursor.close()
            db.close()


if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]
    select_states(username, password, db_name, state_name)
