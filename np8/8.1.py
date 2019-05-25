#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 8.1.py
#purpose : A script to create a line graph with random data input.
#date : 2017.11.1
#version : 1.1

import matplotlib.pyplot as plt
from random import randint

count = 0
num=[]

while count <= 25:
    random = randint(10,100)
    count=count+1
    num.append(random)
print(num)

plt.plot(num, color='black')

plt.xlabel("X axis - Random numbers")
plt.ylabel("Y axis")
plt.title("Line graph of random numbers")

plt.show()
