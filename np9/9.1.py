#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 9.1.py
#purpose : A script to create a pie chart with car theft CSV.
#date : 2017.11.8
#version : 1.1

import matplotlib.pyplot as plt
import csv
import os
import requests
from prettytable import PrettyTable

csv_url = "https://storage.googleapis.com/co-publicdata/county-muni-timeseries.csv"
file_name = 'url_file.csv'

dwnld = requests.get(csv_url) # gets the csv in the dwnld handle

years = []  #all the years
pops = []   #all the population
year1 = []  #year 1990
year2 = []  #year 2009
pop1 = []   #pop in 1990
pop2 = []   #pop in 2009

if os.path.isfile(file_name):
    print("File exists")
else:
    with open(file_name, "wb") as file_name:
        print("File not found. Downloading file")
        file_name.write(dwnld.content) # writes the csv from the download handle

table = PrettyTable(["Year", "Population"]) # defines the column names for the table

with open('url_file.csv') as file:
    reader = csv.reader(file)
    column = []
    for column in reader:
        #checks for blank lines
        if column:
            #print(column[0] + ":" + column[1] + ":" + column[2] + ":" + column[3] + ":" + column[4] + ":" + column[5] + ":" + column[6])
            years.append(column[4])
            pops.append(column[5])

            if '1990' in column[4]:
                year1.append(column[4])
                pop1.append(column[5])
                table.add_row([column[4], column[5]])

            if '2009' in column[4]:
                year2.append(column[4])
                pop2.append(column[5])
                table.add_row([column[4], column[5]])
    #print(year1)
    print("pop in 1990 is")
    print(pop1)
    #print(year2)
    print("pop in 2009 is")
    print(pop2)

    print(table)

    #print(years)
    #print

plt.plot(pop1)
plt.plot(pop2)
plt.legend(['popln in 1990', 'popln in 2009'], loc = 'upper left')
plt.margins(0.025) # margin or kink in the graph
plt.ylabel("Population")
#plt.yticks(rotation = 30)

plt.show()

