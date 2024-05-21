#!/usr/bin/python3
"""
akes in the name of a state as an argument and lists all cities
"""

import MySQLdb
import sys


def filtercities(usname, passwrd, dbname, state):

    db = MySQLdb.connect(host='localhost', user=usname, passwd=passwrd,
                         db=dbname)
    cur = db.cursor()
    query = ('SELECT DISTINCT cities.name FROM cities INNER JOIN states'
             ' ON cities.state_id = states.id WHERE states.name=%s')
    cur.execute(query, (state,))

    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()


if __name__ == '__main__':
    filtercities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
