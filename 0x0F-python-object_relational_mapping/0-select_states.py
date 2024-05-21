#!/usr/bin/python3

"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def states(user, passwrd, db):
    """
    lists all states from the database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=passwrd, db=db)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    dat = cursor.fetchall()

    for i in dat:
        print(i)
    db.close()


if __name__ == '__main__':
    states(sys.argv[1], sys.argv[2], sys.argv[3])
