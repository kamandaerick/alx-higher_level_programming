#!/usr/bin/python3
'''Takes in state name and lists cities in that state'''
import MySQLdb
import sys
'''Access the database and execute the querries'''
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name=%s"
    cur.execute(query, (sys.argv[4], ))
    rows = cur.fetchall()
    r = tuple()
    for row in rows:
        r += row
    print(", ".join(map(str, r)))

    cur.close()
    db.close()
