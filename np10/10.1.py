#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 10.1.py
#purpose : A script to create a GUI with 3 buttons.
#date : 2017.12.1
#version : 1.1

from tkinter import *
import  subprocess
from subprocess import PIPE, Popen
import requests
from lxml.html import fromstring

root = Tk()

root.geometry('580x480')

root.title("HW 10")

def endWindow():
    root.destroy()

def ipLook():
    p = subprocess.check_output(["nslookup", "+short", "www.colorado.edu"])
    display.configure(text=p)
    #print(p)

def getTitle():
    res = requests.get('http://www.colorado.edu')
    #res.text
    #p1 = Popen(["curl", "-L", "http://www.colorado.edu"], stdout=PIPE)
    #p1 = Popen(res.text, stdout=PIPE)
    #p2 = Popen(["grep", "<title>"], stdin=p1.stdout, stdout=PIPE)
    #p1.stdout.close()
    #res1 = p2.communicate()[0]
    #res1 = subprocess.check_call(["curl  -L  http://www.colorado.edu | grep '<title>'"], shell=True)
    #res1 = subprocess.check_output(["curl", "-L", "http://www.colorado.edu", "grep", "<title>"])
    #display.configure(text=res1)
    #print(res1)
    #url = "www.colorado.edu"
    #t = lxml.html.parse(url)
    #print(t.find(".//title").text)
    t = fromstring(res.content)
    title = t.findtext('.//title')
    #print(title)
    display.configure(text=title)

Label(root, text="HW 10").grid(row=1, column=2, columnspan=1, ipadx="180")
display = Label(root, text="")
display.grid(row=3, column=1, columnspan=3)


Button(root, text="Get IP of CU", command= lambda : ipLook()).grid(row=2, column=1)
Button(root, text="Grab Title", command= lambda : getTitle()).grid(row=2, column=2)
Button(root, text="End Program", command= lambda : endWindow()).grid(row=2, column=3)


root.mainloop()
