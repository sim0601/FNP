#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 6.1.py
#purpose : A script to connect to an FTP server and get data
#date : 2017.10.20
#version : 1.1

import sys
import os
from ftplib import FTP

def checkArg():
    if len(sys.argv) != 3:
        print("Error: Enter server name and path to file!" + sys.argv[0])
        sys.exit()
    else:
        return sys.argv[1]

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def get_fromS():
    ftp = FTP('ftp.redhat.com') # connect to host over default port
    ftp.getwelcome() # checks for connection
    ftp.login() # login using anonymous
    ftp.cwd('redhat') # changes into the parent directory
    ftp.retrlines('LIST') #lists the directory contents
    file = open('redhat', 'wb')
    ftp.retrbinary('RETR redhat', file.write)
    #ftp.dir()
    ftp.quit()

def readFile(fileName):
    print("File name is: " + fileName)
    fo = open(fileName, "r")
    file_len = 0
    for line in fo:
        file_len = len(line)
    print("The length of the file is : " + str(file_len))
    fo.close()
    sys.exit()

serverName = sys.argv[1]
fileName = sys.argv[2]

checkArg()
checkFile(fileName)
get_fromS()
readFile(fileName)
