#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 9.2.py
#purpose : A script to create line graphs from the population csv and census website data
#date : 2017.11.8
#version : 1.1

import matplotlib.pyplot as plt
import os
import sys
import subprocess
from prettytable import PrettyTable

file1 = 'output1.txt'
file2 = 'output2.txt'
num = 2
#num = 49
count1 = 0
count2 = 0
Host1 = "8.8.8.8"
Host2 = "4.2.2.1"

if os.path.isfile(file1):
    print("Ping 1 results file found. Updating file")

with open('output1.txt', 'wb') as out:
    while count1 <= num:
        out.write(subprocess.check_output("ping 8.8.8.8")) # writes the data from the ping to the file
        count1 = count1 + 1
        print(str(count1) + " for output 1")

if os.path.isfile(file2):
    print("Ping 2 results file found. Updating file")

with open('output2.txt', 'wb') as out:
    while count2 <= num:
        out.write(subprocess.check_output("ping 4.2.2.1"))
        count2 = count2 + 1
        print(str(count2) + " for output 2")

with open(file1,'r') as fo1:
    RTT1 = ""
    rtt1 = []
    for line in fo1:
        if "Average" in line:
            RTT1 = line.split(" ")
            rtt1.append(RTT1[12])
            #table.add_row([RTT1[12]])
    print(RTT1)
    #print(RTT1[12])
    print(rtt1)
    fo1.close()

with open(file2,'r') as fo2:
    RTT2 = ""
    rtt2 = []
    for line in fo2:
        if "Average" in line:
            RTT2 = line.split(" ")
            rtt2.append(RTT2[12])
    #print(RTT2[12])
    print(rtt2)
    #print(rtt2[0])
    #print(rtt2[1])
    fo2.close()

#table.add_row([rtt1[0], rtt1[1]])
#table.add_row([rtt2[0], rtt2[1]])
table = PrettyTable(["Hosts", "RTT"])
#table.add_column("RTT", [rtt1])
table.add_row([Host1, rtt1])
table.add_row([Host2, rtt2])
print(table)

plt.plot(rtt1)
plt.plot(rtt2)
plt.legend(['Host1', 'Host2'], loc = 'upper left')
plt.margins(0.025)
plt.ylabel("Avg. RTT")
plt.show()
