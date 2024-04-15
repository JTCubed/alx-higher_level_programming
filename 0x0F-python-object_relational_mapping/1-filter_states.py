#!/usr/bin/python3

"""
 lists all states with a name starting with N
"""

import sys
import MySQLdb



def city_name(usname, passwrd, dbname):
    """
    lists all states with a name starting with N
    """
    db = MySQLdb.connect(host='localhost',port=3306, user=usname,
                         passwd=passwrd, db=dbname)

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name like "N%" ORDER BY states.id ASC')
    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()

if __name__ == '__main__':
    city_name(sys.argv[1], sys.argv[2], sys.argv[3])
