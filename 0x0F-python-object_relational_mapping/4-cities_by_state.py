#!/usr/bin/python3
import MySQLdb
import sys
""" This script uses JOIN to list cities in every state"""


def list_cities_by_state(username, password, db_name):
    """Function to handle to connect to the datase and handle the query

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
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query)
        cities = cursor.fetchall()
        for city in cities:
            city_id, city_name, state_name = city[0], city[1], city[2]
            print(f"({city_id}, '{city_name}', '{state_name}')")

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if 'db' in locals() and db.open:
            cursor.close()
            db.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]
    list_cities_by_state(username, password, db_name)
