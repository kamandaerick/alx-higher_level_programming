#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa,
ordered by city id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    db = MySQLdb.connect(
      host="localhost",
      port=3306,
      user=sys.argv[1],
      passwd=sys.argv[2],
      db=sys.argv[3]
      )
    
    c = db.cursor()

    c.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
               FROM `cities` \
               INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` \
               ORDER BY `cities`.`id`")

    [print(city) for city in c.fetchall()]

    c.close()
    db.close()
