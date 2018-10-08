#Team Typers-Tianrun Liu and Kyle Tau
#SoftDev1 pd6
#K17 -- Average
#2018-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

db = sqlite3.connect("sp_database.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#
#**************FILL TABLE COURSES********************
#
#open and read csv file
file = open('data/courses.csv')
reader = csv.reader(file)
#
#create courses table
command = "CREATE TABLE courses(code TEXT,mark INTEGER,id INTEGER)"
c.execute(command)    #run SQL statement
#
#add data by key into table
for row in reader:
	command2 = 'INSERT INTO courses VALUES(?,?,?)'
	c.execute(command2,row)
#
#**************FILL TABLE PEEPS********************
#
#open and read csv file
file = open('data/peeps.csv')
new_reader = csv.reader(file)
#
#create peeps table
command3 = "CREATE TABLE peeps(name TEXT,age INTEGER,id INTEGER)"
c.execute(command3)
#
#add data by key into table
for row in new_reader:
	command4 = 'INSERT INTO peeps VALUES(?,?,?)'
	c.execute(command4,row)
#
#==========================================================
#
#*************ACCESS STUDENT GRADE*****************
def stu_grade(stu_id):
	c.execute("select name, code, mark from peeps, courses where peeps.id = ? and courses.id = peeps.id",[stu_id])
	result = c.fetchall()
	for r in result:	#https://www.python-course.eu/sql_python.php
		print(r)	
	return ""

def all_stu_grade():
	c.execute("select name, code, mark from peeps, courses where peeps.id = courses.id")
	result = c.fetchall()
	for r in result:	
		print(r)	
	return ""

def stu_average(stu_id):
	c.execute("select mark from courses where courses.id = ?",[stu_id])
	result = c.fetchall()
	i = 0;
	counter = 0;
	for r in result:	
		i += int(r[0])
		counter += 1
	result = int(i/counter)
	print("student with id = " + str(stu_id) + "'s average is " + str(result))	
	return result

def all_stu_average():
	c.execute("select name, id from peeps")
	result = c.fetchall()
	for r in result:
		try:
			stu_average(r[1])
		except:
			pass #this will skip the first row in result, which is not an integer and will cause an error
	return ""

#=======================CREATE TABLE peeps_avg============================
command3 = "CREATE TABLE peeps_avg(id INTEGER,average INTEGER)"
c.execute(command3)
#
#########################################################################
#USE MODULAR DESIGN#USE MODULAR DESIGN#USE MODULAR DESIGN
#########################################################################
for r in range(10):
	c.execute("INSERT INTO {} VALUES({},{})".format("peeps_avg",r+1,stu_average(r+1)))
#
#db.commit()
#===========================================================================
		
def addRow(code, mark, id):                                              #facilitates adding row to courses
	c.execute("INSERT INTO courses VALUES ({},{},{})".format(code, mark, id))

def display():
	print("================ALL STUDENTS AND AVERAGES=================")
	for r in range(10):
		c.execute("select name from peeps where id = {}".format(r+1))
		result1 = c.fetchall()
		c.execute("select * from peeps_avg where id = {}".format(r+1))
		result2 = c.fetchall()
		print(result1+result2)

display()
#print("=======================DEMO fetch student grade==================");
#stu_grade(1)
#print("=======================DEMO fetch all student grade==============");
#all_stu_grade()
#print("=======================DEMO calc student average=================");
#stu_average(1)
#print("=======================DEMO all student average==================");
#all_stu_average()

#db.commit() #save changes #test code
#print("**************************COURSES*********************************")
#c.execute("SELECT * FROM courses")
#print(c.fetchall())
#print("**************************PEEPS*********************************")
#c.execute("SELECT * FROM peeps")
#print(c.fetchall())
#print("*************************PEEPS_AVG**********************************")
#c.execute("SELECT * FROM peeps_avg")
#print(c.fetchall())
db.close() #close database
