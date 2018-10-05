#Team Go -- Angela Tom, Kyle Tau
#SoftDev1 pd6
#K16 -- No Trouble
#2018-10-05

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)"          #init table for peeps
c.execute(command)    #run SQL statement
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"       #init table for courses
c.execute(command)

def populate():
    with open('data/peeps.csv') as infile: #populate peeps
        peepsR = csv.DictReader(infile)
        for row in peepsR:
            c.execute("INSERT INTO peeps VALUES ('" +row['name']+ "'," +row['age']+ "," +row['id']+ ")") #add for every row

    with open('data/courses.csv') as infile: #populate courses
        coursesR = csv.DictReader(infile)
        for row in coursesR:
            c.execute("INSERT INTO peeps VALUES ('" +row['code']+ "'," +row['mark']+ "," +row['id']+ ")") #add for every row

populate()
#==========================================================

db.commit() #save changes
db.close()  #close database


