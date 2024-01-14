#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
    the code is not executed when imported
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
            FROM `states` \
            ORDER BY `id`")
    table = cur.fetchall()
    for row in table:
        if row[1] == sys.argv[4]:
            print(row)