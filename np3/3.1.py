#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 3.1.py
#purpose : A script to read files and print lines
#date : 2017.09.15
#version : 1.1

import sys
import os

def checkArg():
    global fileName
    fileName = sys.argv[1]
    if len(sys.argv) != 2:
        print("Error: Give a file name!" + sys.argv[0])
        sys.exit()
    #return sys.argv[1]

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def readFile(fileName):
    print("File name is: " + fileName)
    fo = open(fileName, "r")
    line_len = 0
    for line in fo:
        current_len = len(line)
        if current_len > line_len:
            line_len = current_len
            long_line = line
            long_len = current_len
    print("The longest line was: " + long_line)
    print("The length of the longest line is : " + str(long_len))
    fo.close()
    sys.exit()



checkArg()
checkFile(fileName)
readFile(fileName)
















