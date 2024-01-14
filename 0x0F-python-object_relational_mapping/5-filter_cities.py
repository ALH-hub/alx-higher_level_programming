#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_0_usa
    the code is not executed when imported
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` \
                INNER JOIN `states` \
                   ON cities.state_id = states.id \
                ORDER BY cities.id")
    print(", ".join([row[2] for row in cur.fetchall()
                     if row[4] == sys.argv[4]]))
