#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
    the code is not executed when imported
"""
import sys
import MySQLdb


if name = "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    table = cur.fetchall()
    print(table)
