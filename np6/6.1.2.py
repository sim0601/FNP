#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 6.1.py
#purpose : A script to connect to an FTP server and get data
#date : 2017.10.21
#version : 1.2

import sys
from ftplib import FTP
import os

local_file = 'README_orig' # this is the pre-downloaded file used to compare the size from the file downloaded from the server(README)
down_file = 'README'

def checkArg():
    if len(sys.argv) != 3:
        print("Error: Enter server name and path to file!" + sys.argv[0])
        sys.exit()
    else:
        return sys.argv[1]
        return sys.argv[2]

def checkFile(local_file, down_file):
    print("The local file is: " + local_file)
    if os.path.isfile(local_file):
        print("Local file exists")
    else:
        print("Local file not found")
    print("The downloaded file is: " + down_file)
    if os.path.isfile(down_file):
        print("Downloaded file found")
    else:
        print("Downloaded file not found")
        sys.exit()

def readFile(local_file, down_file):
    local_f = open(local_file, 'r')
    file_len = 0
    for line in local_f:
        curr_len = len(line)
        if curr_len > file_len:
            file_len = curr_len
    print("The length of the local file is : " , file_len)
    local_f.close()

    down_f = open(down_file, 'rb')
    file_len_d = 0
    for line in down_f:
        curr_len = len(line)
        if curr_len > file_len_d:
            file_len_d = curr_len
    print("The length of the downloaded file is : " , file_len_d)
    down_f.close()

    if file_len == file_len_d:
        print("Successful download")
    else:
        print("Download not successful")

    sys.exit()

def get_data():

    ftp = FTP(server_name) #connect to the ftp server
    print("Welcome!", ftp.getwelcome()) # to check if connection is valid
    if ftp.getwelcome() == ' ':
        print("Server connection not successful")
    else:
        ftp.login()
        print(ftp.login())
        if ftp.login() == ' ':
            print("Login to server not successful")
        else:
            print(ftp.cwd(file_path)) # access the directory where the file is. Path exculding the actual file is needed
            if ftp.cwd(file_path) == ' ':
                print("Directory not found")
                print("Unable to download requested file")
            else:
                down_f = open('README', 'wb')
                ftp.retrbinary('RETR README', down_f.write) # retrieve and write contents to a file called README o the local system
                down_f.close()

    ftp.quit()

server_name = sys.argv[1] #this is 'ftp.redhat.com'
file_path = sys.argv[2] # this is '/pub/redhat/linux'

checkArg()
get_data()
checkFile(local_file, down_file)
readFile(local_file, down_file)

