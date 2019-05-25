#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 5.2.py
#purpose : A script to print planet info after reading from a database
#date : 2017.10.04
#version : 1.1

import sys
import os
import sqlite3

DBname = sqlite3.connect('planetDB.db')
DBname.row_factory = sqlite3.Row
cursor = DBname.cursor()

def checkArg():
    if len(sys.argv) != 2:
        print("Error: Enter listing option!" + sys.argv[0])
        sys.exit()
    else:
        return sys.argv[1]

def checkDB(DBname):
    db = str(DBname)
    print("The database you are searching is: " + db)
    if os.path.isfile("planetDB.db"):
        print("Database found")
    else:
        print("Database not found")
        sys.exit()

def queryDB(DBname, option):
    print("To list planets by distance, enter 'distance'")
    print("To list palnets by mass, enter 'mass'")
    print("To list planets alphabetically enter, 'alphabet'")
    print("The list option you entered is: " + option)

    if option == 'distance':
        query = "select Name, Distance from planets order by Distance"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("The planets listed by distance are: ")
        for row in rows:
             print(row[0])
        sys.exit()

    if option == 'mass':
        query = "select Name, Mass from planets order by Mass"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("The planets listed by mass are: ")
        for row in rows:
             print(row[0])
        sys.exit()

    if option == 'alphabet':
        query = "select Name from planets order by Name"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("The planets listed alphatebetically are: ")
        for row in rows:
             print(row[0])
        sys.exit()

    else:
        sys.exit()

option = sys.argv[1]

checkArg()
checkDB(DBname)
queryDB(DBname, option)
