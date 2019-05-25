usr#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 8.3.py
#purpose : A script to create a pie chart with car theft CSV.
#date : 2017.11.1
#version : 1.1

import matplotlib.pyplot as plt
import csv
import os
import sys

fileName = "cartheft.csv"

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def plot():
    # plot the pie chart
    make=[]
    model=[]
    thefts=[]
    production=[]
    rate=[]
    year=[]
    type_c=[]
    make1=[]

    with open('cartheft.csv') as file:
        reader = csv.reader(file)
        column = []
        for column in reader:
            #checks for blank lines
            if column:
                #print(column[0].rjust(20) + ":" + column[4].rjust(10) + ":" + column[6].rjust(10))
                make.append(column[0])
                rate.append(column[4])
                type_c.append(column[6])

                if 'Car' in column[6] and column[4] >= '2.5': #doesnt give results when replaced with type_c and rate
                    make1.append(column[0])
                    model.append(column[1])
                    thefts.append(column[2])

        print(make1)
        print(model)
        print(thefts)

    perc = [int(thefts[0])/100, int(thefts[1])/100, int(thefts[2])/100,int(thefts[3])/100,int(thefts[4])/100,int(thefts[4])/100,int(thefts[6])/100,int(thefts[7])/100,
            int(thefts[8])/100,int(thefts[9])/100,int(thefts[10])/100,int(thefts[11])/100,int(thefts[12])/100,int(thefts[13])/100]

    '''for n in thefts[n] >= 0:
        perc = [int(thefts[n])/100]
        perc.append(perc)'''

    plt.title("Car Theft")
    plt.pie(perc, labels=model, autopct='%0.2f%%', shadow=True, startangle=90)
    plt.show()

checkFile(fileName)
plot()


'''autopct enables you to display the percent value using Python string formatting. For example, if autopct='%.2f',
 then for each pie wedge, the format string is '%.2f' and the numerical percent value for that wedge is pct,
  so the wedge label is set to the string '%.2f'%pct.'''

'''0.1 means one digit after decimal, 0.2 means 2 dgits after decimal'''
