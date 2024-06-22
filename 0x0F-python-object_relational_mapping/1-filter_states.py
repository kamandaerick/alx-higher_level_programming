#!/usr/bin/python3
"""List all states with a name starting with N from the db"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Establish a connection to the database
        db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db_connection.cursor()

        # Execute an SQL query to select states with names starting with 'N' in ascending order by id
        query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the results
        rows = cursor.fetchall()

        # Process and print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")

    finally:
        # Ensure resources are closed properly
        if cursor:
            cursor.close()
        if db_connection:
            db_connection.close()

