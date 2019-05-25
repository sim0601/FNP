#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 4.2.py
#purpose : A script that takes filename and planet names as arguments
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
    print("You entered planet: " + planetName )
    fo = open(fileName, "r")
    planets = {}

    for line in fo:
        planet = {}
        (planet['Name'], planet['Mass'], planet['Diameter'], planet['Distance'], planet['Moons']) = line.split()
        planets[planet['Name']] = planet # creates local dict for each planet where the planet name is the key and the other data is the value

    if planetName in planets:
        print(planets[planetName])

    else:
        print("Invalid planet name")
        sys.exit()



    fo.close()
    sys.exit()


fileName = sys.argv[1]
planetName = sys.argv[2]

checkFile(fileName)
readFile(fileName)

