#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 7.1.py
#purpose : A script to create a web server in flask that will query a database and accept user input.
#date : 2017.10.26
#version : 1.3


from flask import Flask, render_template, request
import sqlite3
import sys
import os

app = Flask(__name__)

@app.route('/') # the route decorator tells flask which URL you should trigger our function
def Index(): # the function is given a name which is used to gernerate URLs for that function
    return render_template('Index.html')

@app.route('/page1', methods=['GET','POST']) # to query a database and return its contents
def page1():
    if request.method == 'GET':
        DBname = sqlite3.connect('planetDB.db')
        DBname.row_factory = sqlite3.Row
        cursor = DBname.cursor()
        query = "select * from planets "
        cursor.execute(query, )
        rows = cursor.fetchall()
        planets =[]
        for row in rows:
            planet = {}
            (planet['Name']) = row[0]
            (planet['Mass']) = row[1]
            (planet['Distance']) = row[2]
            planets.append(planet) #list containing dicts
        bodyText = planets
        return render_template('page1.html', bodyText=bodyText)

@app.route('/page2',methods=['GET','POST'])  # query a database from a form using user input
def page2():
    return render_template('page2.html')

@app.route('/formData', methods=['GET','POST'])
def formData():
    if request.method == 'POST':
        planetName=request.form['planetName']
        if os.path.isfile('planetDB.db'):
            DBname = sqlite3.connect('planetDB.db')
            DBname.row_factory = sqlite3.Row
            cursor = DBname.cursor()

            print("The planet name you entered is: " + planetName)

            query = "select * from planets where Name=?"
            t=(planetName,)
            cursor.execute(query, t)
            rows = cursor.fetchall()

            if len(rows) != 0: # checks for a blank DB
                for row in rows:
                    planet = {}
                    (planet['Name']) = row[0]

                    if planetName in row[0]:
                        return (str(row[1]) + " is the mass of " + str(row[0]) + " " + str(row[2]) + " is the distance of  " +  str(row[0]) + " " + "from the sun")
            else:
                return ( "Planet name " + planetName + " entered is not valid. Please enter planet name in all CAPS")

            sys.exit()

        else:
            return("Database not found")


if __name__=='__main__':
    app.debug = True
    app.run(host='127.0.0.1', port =8080)
