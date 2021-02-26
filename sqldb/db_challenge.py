#!/usr/bin/env python3

import sqlite3


def createdb():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
    (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
     AGE            INT     NOT NULL,
    ADDRESS        CHAR(50),
    SALARY         REAL);''')
    print("Table created successfully")
    return 
    conn.close()


def insertdb():
    conn = sqlite3.connect('test2.db')
    print("Opened database successfully")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

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


