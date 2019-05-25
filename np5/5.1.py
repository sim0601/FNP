#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 5.1.py
#purpose : A script to print state names from abbreviations after reading from a database
#date : 2017.10.04
#version : 1.1

import sys
import os
import sqlite3

DBname = sqlite3.connect('stateDB.db')
DBname.row_factory = sqlite3.Row
cursor = DBname.cursor()

def checkArg():
    if len(sys.argv) != 2:
        print("Error: Enter an abbreviation!" + sys.argv[0])
        sys.exit()
    else:
        return sys.argv[1]

def checkDB(DBname):
    db = str(DBname)
    #print(db)
    print("The database you are searching is: " + db)
    if os.path.isfile("stateDB.db"):
        print("Database found")
    else:
        print("Database not found")
        sys.exit()

def queryDB(DBname, abv):
    print("The state abbreviaiton you entered is: " + abv)
    query = "select * from States where Abbrv=?"
    t=(abv,)
    cursor.execute(query, t)
    rows = cursor.fetchall()
    for row in rows:
        print(row[1] + " is the abbreviation of " + row[0])
    sys.exit()

abv = sys.argv[1]

checkArg()
checkDB(DBname)
queryDB(DBname, abv)
