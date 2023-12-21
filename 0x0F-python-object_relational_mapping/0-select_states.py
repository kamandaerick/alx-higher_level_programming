#!/usr/bin/python3

"""
This script prints the states in the states table
in the following format (id, name)
"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=db_name)
c = db.cursor()

querry = "SELECT * FROM states ORDER BY states.id"

c.execute(querry)

states = c.fetchall()

for state in states:
    state_id = state[0]
    state_name = state[1]
    
    print(f"({state_id}, '{state_name}')")

c.close()
db.close()

