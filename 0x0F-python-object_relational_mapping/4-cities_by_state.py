#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_0_usa
    the code is not executed when imported
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM `cities` \
            INNER JOIN `states` \
            ON cities.id = states.id \
            ORDER BY cities.id")
    table = cur.fetchall()
    for row in table:
        print(row)
