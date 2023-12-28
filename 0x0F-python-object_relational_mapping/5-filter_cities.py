#!/usr/bin/python3
"""
This script lists all cities in a state provided
as an argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        host='localhost',
        port=3306,
        db=database_name
    )

    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    result = ", ".join(city[0] for city in cities)
    print(result)

    cursor.close()
    db.close()
