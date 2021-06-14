#!/usr/bin/env python3

# standard library
import csv
import os
import time

# reading from csv file and storing in variable comicfile 
with open("brett_comics.txt", "r") as comicfile:
    
    reader = csv.reader(comicfile)
    comicList = list(reader)

    # function to take input of user, read the csv file and display only elements from that input

def comicReader(reader):
    comicInput = input("""
            
                       What kind of comics would you like to view in my collection? 
                       1. Spider-man
                       2. Batman
                       3. Superman
                       4. X-men
                       5. Dont want to view anything
                       """)
    # while loop to display ASCII and list comics by title 
    # loop will exit when user pick's option 5
    while comicInput != "6":
        if comicInput == "1":
            os.system("clear")
            with open("/home/student/mycode/spiderman.txt") as spidey:
                print(spidey.read())
            time.sleep(3)
            print("This is what I have for Spider-Man in my collection")


comicReader(reader)
