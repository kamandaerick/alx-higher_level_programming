#!/usr/bin/python3
import MySQLdb
import sys
"""Take the name of a state as an argument and prints cities"""


def filter_cities_by_state(username, password, db_name, state_name):
    """Take the name of a state and list its cities

    Args:
        username (string): username
        password (string): password
        db_name (string): database name
        state_name (string): name of a state
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
                "SELECT GROUP_CONCAT(DISTINCT cities.name "
                "ORDER BY cities.id ASC SEPARATOR ', ') "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s"
            )

        cursor.execute(query, (state_name,))
        result = cursor.fetchone()[0]
        if result:
            print(result)
        else:
            print("")
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if 'db' in locals() and db.open:
            cursor.close()
            db.close()


if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]
    filter_cities_by_state(username, password, db_name, state_name)
