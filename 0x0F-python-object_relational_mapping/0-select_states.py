#!/usr/bin/python3
"""list all states from the database hbtn_0e_usa"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

db_connection = MySQLdb.connect(
        host = 'localhost',
        user = username,
        passwd = password,
        port = 3306,
        db = db_name
        )

cursor = db_connection.cursor()
cursor.execute('SELECT * FROM states')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db_connection.close()
