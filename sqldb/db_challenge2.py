#!/usr/bin/env python3

import sqlite3


def createdb(tab_name):
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS {tab_name}
    (ID INT PRIMARY KEY     NOT NULL,
    FNAME           TEXT    NOT NULL,
    COLOR           TEXT     NOT NULL,
    TASTE           CHAR(50),
    RATING         INT);''')
    print("Table {tab_name} created successfully")
    conn.close()


def insertdb():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")

    conn.execute("INSERT INTO COMPANY (ID,FNAME,COLOR,TASTE,RATING) VALUES (1, 'Mango', 'Yellow', 'Sweet', 100 )")

    conn.execute("INSERT INTO COMPANY (ID,FNAME,COLOR,TASTE,RATING) VALUES (2, 'Banana', 'Green', 'Yum', 75 )")

    conn.execute("INSERT INTO COMPANY (ID,FNAME,COLOR,TASTE,RATING) VALUES (3, 'Grapes', 'Red', 'Sour', 50 )")

    conn.execute("INSERT INTO COMPANY (ID,FNAME,COLOR,TASTE,RATING) VALUES (4, 'Kiwi', 'Brown', 'Yuck', 25 )")

    conn.commit()
    print("Records created successfully")
    conn.close()


def selectdb():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()


def updatedb():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")
    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    cursor1 = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor1:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()

def deletedb():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")
    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    cursor2 = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor2:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()

if __name__ == "__main__":
    createdb()
    insertdb()
    selectdb()
    updatedb()
    deletedb()


