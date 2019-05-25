#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 4.1.py
#purpose : A script to read files and sort data using hashes
#date : 2017.09.25
#version : 1.2

import sys
import os

def checkArg():
    if len(sys.argv) != 2:
        print("Error: Give a file name!" + sys.argv[0])
        sys.exit()
    return sys.argv[1]

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile("planetinfo.txt"):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def readFile(fileName):
    print("File name is: " + fileName)
    c = input("Do you want to list by 1. distance or 2. mass: ")
    choice = int(c)
    fo = open(fileName, "r")
    planets = {}
    if choice == 1:
        planets_dist = []
        for line in fo:
            planet = {}
            (planet['Name'], planet['Mass'], planet['Diameter'], planet['Distance'], planet['Moons']) = line.split()
            #print(type(planet['Name']))
            planets_dist.append(planet) #list containing dicts
            #print(planet)
        #print(planets_dist)
        print("The planets sorted by distance are:")
        print(sorted(planets_dist, key = lambda x : float(x['Distance']))) # defines a function called x which is the key, and the key is the float value of distance
        sys.exit()

    if choice == 2:
        planets_m = []
        for line in fo:
            planet = {}
            (planet['Name'], planet['Mass'], planet['Diameter'], planet['Distance'], planet['Moons']) = line.split()
            planets_m.append(planet) #list containing dicts
            #print(planet)
        print(planets_m)
        print("The planets sorted by mass are:")
        print(sorted(planets_m, key = lambda x : float(x['Mass']))) # sorts planets_m by each line x defined by key Mass

    fo.close()
    sys.exit()


fileName = sys.argv[1]

checkFile(fileName)
readFile(fileName)

