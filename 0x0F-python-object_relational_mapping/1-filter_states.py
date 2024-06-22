#!/usr/bin/python3
"""List states whose name starts with N from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 4:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    else:
        print("Usage: ./1-filter_states.py username password database_name")
        exit(1)

