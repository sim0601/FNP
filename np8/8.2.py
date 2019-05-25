#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 8.2.py
#purpose : A script to create a bar graph with state population CSV.
#date : 2017.11.2
#version : 1.2

import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys

fileName = "statepop.csv"

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def plot():
    # x and y will be read from the CSV
    xaxis=[] #states
    yaxis=[] #population

    with open('statepop.csv') as file:
        reader = csv.reader(file)
        column = []
        for column in reader:
            #checks for blank lines
            if column:
                print(column[0].rjust(20) + ":" + column[1].rjust(10))
                xaxis.append(column[0])
                yaxis.append(column[1])


    barWidth=0.5

    plt.bar(xaxis, yaxis, barWidth, color='g')

    plt.xlabel("States")
    plt.xticks(rotation='vertical')
    #plt.yticks(rotation=90)
    plt.ylabel("Population")
    plt.title("States and their Popultion")

    plt.show()

checkFile(fileName)
plot()
