#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table of hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter(usname, passwrd, dbname, searched):
    """
    takes in arguments and displays all values in the states table of
    hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=usname,
                         passwd=passwrd, db=dbname)
    cur = db.cursor()
    statement = 'SELECT * FROM states WHERE name = %s ORDER BY id ASC'
    cur.execute(statement, (searched,))

    o = cur.fetchall()

    for i in o:
        print(i)

    cur.close()
    db.close


if __name__ == '__main__':
    filter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
