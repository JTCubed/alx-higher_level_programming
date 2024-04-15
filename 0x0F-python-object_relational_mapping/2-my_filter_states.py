#!/usr/bin/python3

"""
takes in an argument and displays all values
"""

import MySQLdb
import sys

def filter(usname, passwrd, dbname, searched):
    """
    takes in an argument and displays all values
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=usname,
                       passwd=passwrd, db=dbname)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name = %s', (searched,))

    o = cur.fetchall()

    for i in o:
        print(i)

    cur.close()
    db.close

if __name__ == '__main__':
    filter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
