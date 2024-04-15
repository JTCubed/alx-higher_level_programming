#!/usr/bin/python3

import sys
import MySQLdb

def citystates(usname, passwrd, dbname):
    db = MySQLdb.connect(host='localhost', port=3306, user=usname,
                         passwd=passwrd, db=dbname)

    cur = db.cursor()
    query = 'SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC'
    cur.execute(query)

    o = cur.fetchall()
    for i in o:
        print(i)
    cur.close()
    db.close()


if __name__ == '__main__':
    citystates(sys.argv[1], sys.argv[2], sys.argv[3])
