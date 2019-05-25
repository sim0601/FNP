#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 3.2.py
#purpose : A script to read files and print a sorted list
#date : 2017.09.15
#version : 1.1

import sys
import os

def checkArg():
    if len(sys.argv) != 2:
        print("Error: Give a file name!" + sys.argv[0])
        sys.exit()
    return sys.argv[1]

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile("file1.txt"):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def read_sort(fileName):
    print("File name is: " + fileName)
    fo = open(fileName)
    c = input("Enter 1. for forward sort and 2. for reverse sort: ")
    choice = int(c)
    if choice == 1:
        for lines in fo:
            words = lines.strip().split(' ') # creates a list of words
            #print(type(words))
            print(sorted(words))
    if choice == 2:
        for lines in fo:
            words = lines.strip().split(' ')
            print(sorted(words, reverse = True))
            #or we can use words.sort() then print words becuase value stored in words again when using sorted
    else:
        sys.exit()
    fo.close()

fileName = sys.argv[1]

checkArg()
checkFile(fileName)
read_sort(fileName)
















