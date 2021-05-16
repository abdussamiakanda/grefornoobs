import re
import datetime
import random
from datetime import datetime
from PyDictionary import PyDictionary
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import requests


def start():
    f = open("progress.txt","a")
    f.writelines(["# Data:False\n"])
    f.close()


def hello():
    f = open("progress.txt","r")

    lines = f.readlines()
    lin = lines[0].split(":")

    f.close()

    f1 = open("progress.txt","a")
    if lin[1] == "False\n":
        print("Welcome to the GRE for Noobs python package. This package will help you through your GRE preparation.\n")
        a = input("Enter your name: ")
        b = input("Enter your email: ")
        x = datetime.datetime.now()
        f1.writelines(["# Name:",a,"\n"])
        f1.writelines(["# Email:",b,"\n"])
        f1.writelines(["# Date:",str(x),"\n"])
        with open("progress.txt", 'r+') as f:
            text = f.read()
            text = re.sub('False', 'True', text)
            f.seek(0)
            f.write(text)
            f.truncate()

    if lin[1] == "True\n":
        print("Hello",lines[1][7:])

    f1.close()

    
def new():
    a = input("Enter the word: ")
    b = input("Enter meaning of the word: ")
    c = input("Enter the set number: ")

    f = open("vocabulary.txt","a")
    f.writelines([c,":",a,":",b,"\n"])
    f.close()

    
def meaning():
    a = input("Enter the word: ")
    c = 0

    f = open("vocabulary.txt","r")
    for line in f:
        splitLine = line.split(":")

        if splitLine[1] == a:
            print("Meaning:",splitLine[2].replace("\n", ""))
            print("Set:",splitLine[0])
            c = 1

    if c == 0:
        print("The word doesn't exist in the database. Here is the meaning from Google Translate:\n")
        dictionary = PyDictionary(a)
        print(dictionary.printMeanings())
    
    f.close()

    
def set():
    a = int(input("Enter the set number: "))
    print(" ")

    f = open("vocabulary.txt","r")
    for line in f:
        splitLine = line.split(":")

        if int(splitLine[0]) == a:
            print("Word:",splitLine[1])
            print("Meaning:",splitLine[2])
    
    f.close()

    
def exam():
    tot = 0
    n = int(input("Enter the number of words you want to try: "))
    print(" ")
    f = open("vocabulary.txt","r")
    list1 = []
    for line in f:
        splitLine = line.split(":")
        list1.append(splitLine[1])
    f.close()

    xm = random.sample(list1, n)
    for i in range(0,n):
        pop = "Word: "+xm[i]+" "
        c = input(pop)

        f = open("vocabulary.txt","r")
        for line in f:
            splite = line.split(":")

            if splite[1] == xm[i]:
                print("Meaning: "+splite[2].replace("\n", ""))
                mark = int(input("Mark: "))
                print("\n")
                tot += mark

        f.close()
    percent = tot/n*100
    print("Total marks: "+str(tot)+"/"+str(n)+" ("+str(percent)+"%)")

    x2 = datetime.now()
    x3 = x2.strftime("%d %B %Y")

    f1 = open("progress.txt","a")
    f1.writelines(["Mark:",str(x3),":",str(tot),":",str(n),"\n"])
    f1.close()


def flash():
    s = int(input("Enter the set number: "))

    f = open("vocabulary.txt","r")
    for line in f:
        splitLine = line.split(":")

        if int(splitLine[0]) == s:
            pop = "Word: "+splitLine[1]
            c = input(pop)
            print("Meaning:",splitLine[2])
            
    f.close()

    
def progress():
    f = open("progress.txt","r")
    lines = f.readlines()
    f.close()

    print("Hello "+str(lines[1][7:].replace("\n", ""))+". Here is your progress so far.\n")
    lin = lines[3].split(":")
    a = datetime.strptime(lin[1][:10], '%Y-%m-%d')
    b = datetime.now()
    x = (b - a).days
    print("GRE preparation: "+str(x)+" days")
    print("Exams taken: "+str(len(lines)-4))

    M = 0
    N = 0

    f = open("progress.txt","r")
    for line in f:
        splitLine = line.split(":")

        if splitLine[0][0] != "#":
            M += int(splitLine[2])
            N += int(splitLine[3].replace("\n", ""))

    f.close()
    
    f5 = open("vocabulary.txt","r")
    lines5 = f5.readlines()
    f5.close()

    print("Obtained marks: "+str(M/N*100)+"%\n")
    print("Total words in vocabulary: "+str(len(lines5))+"\n")
    print("Exam evolution:")

    x = []
    y = []
    i = 0
    
    f = open("progress.txt","r")
    for line in f:
        splitLine = line.split(":")

        if splitLine[0][0] != "#":
            i += 1
            x.append(i)
            y.append(int(splitLine[2])/int(splitLine[3])*100)

    f.close()

    ax = plt.figure(figsize=(10,2)).gca()
    plt.plot(x,y)
    plt.ylim(0,105)
    plt.xlabel("Exams")
    plt.ylabel("Percentage (%)")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()


def update():
    print("Are you sure? This action might remove the words that you added.")
    ans = input()

    if ans == "y" or ans == "Y" or ans == "Yes" or ans == "yes":
        url = 'https://drive.google.com/uc?export=download&id=1kLBuhoDUUvrJOuBOLUGff0JYr8dB_nQJ'
        r = requests.get(url, allow_redirects=True)
        open('vocabulary.txt', 'wb').write(r.content)
        print("Files are updated.")
        
    elif ans == "n" or ans == "N" or ans == "No" or ans == "no":
        print("Files are not updated.")
        
    else:
        print("Your answer is not acceptable.")




def help():
    print("start() : builds necessary database for the package")
    print("hello() : gets you started with the package")
    print("new() : adds new word of GRE vocabulary")
    print("meaning() : prints out the meaning of a given word")
    print("set() : prints out all the words in a set")
    print("flash() : flashcard of a set")
    print("exam() : takes a random vocabulary quiz")
    print("progress() : shows data about your preparation progress")
    print("update() : updates database from the internet")