#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 6.1.py
#purpose : A script to connect to an FTP server and get data
#date : 2017.10.22
#version : 1.3

import sys
from ftplib import FTP
import os

down_file = 'README'

def checkArg():
    if len(sys.argv) != 3:
        print("Error: Enter server name and path to file!" + sys.argv[0])
        sys.exit()
    else:
        return sys.argv[1]
        return sys.argv[2]

def checkFile(down_file):
    print("The downloaded file is: " + down_file)
    if os.path.isfile(down_file):
        print("Downloaded file found")
    else:
        print("Downloaded file not found")
        sys.exit()

def get_data():
    if sys.argv[1] == server_name:
        try :
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
                    #print(ftp.pwd())
                    if ftp.cwd(file_path) == ' ':
                        print("Directory not found")
                        print("Unable to download requested file")
                    else:
                        down_s = open('README', 'wb')
                        # retrieve and write contents to a file called README to the local system
                        ftp.retrbinary('RETR README', down_s.write)
                        down_s.close()

                        down_s = open('README', 'rb')
                        file_len_s = 0
                        for line in down_s:
                            curr_len = len(line)
                            if curr_len > file_len_s:
                                file_len_s = curr_len
                        print("The length of the file on server is : " , file_len_s)
                        ftp.quit()

                        down_d = open(down_file, 'rb')
                        file_len_d = 0
                        for line in down_d:
                            curr_len = len(line)
                            if curr_len > file_len_d:
                                file_len_d = curr_len
                        print("The length of the downloaded file is : " , file_len_d)
                        down_d.close()

                        if file_len_s == file_len_d:
                            print("Successful download")
                        else:
                            print("Download not successful")
                            sys.exit()
        except Exception:
            print("Server name invalid")

server_name = sys.argv[1] #this is 'ftp.redhat.com'
file_path = sys.argv[2] # this is '/pub/redhat/linux'

checkArg()
checkFile(down_file)
get_data()



