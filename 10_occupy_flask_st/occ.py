#Kyle Tau
#SoftDev1 pd 6
#K10 -- Jinja Tuning
#2018-09-24

from flask import Flask, render_template
app = Flask(__name__)
import csv
import random

file  = open("data/occupations.csv", "r") #open and read the file
occupations = file.readlines() 
file.close() 

#creating occupation dictionary and random occupation function
dictionary = {} #initialize dictionary!
for item in occupations[1:len(occupations)-1]: #add occupation into dictionary, skipping the first line (headers) and the last line (total)
  key = item[:item.rfind(",")] #returns the occupation 
  value = float(item[item.rfind(",")+1:item.rfind("\\")]) #returns the percent corresponding with that application
  dictionary[key] = value  #input key and value into the dictionary
def randOcc():
  val = random.randint(0,998) #threshold
  num = 0
  occ = "" #occupation name
  for i in dictionary: #iterate through the dictionary
    occ = i; #record the occupation
    num += dictionary[i]*10 #add onto num 
    if num >= val: #check to see if it has reached the threshold
      break; #if threshold is met, stop 
  return occ


@app.route('/occupations')
def run():
   return render_template("template.html",
	title = "Occupations",
	heading = "This website displays a table of the occupations and their percentages of the job field in America. The following is a randomly displayed occupation:",
	randOcc = randOcc(),
	occd = dictionary)


if __name__ == "__main__":
     app.debug = True
     app.run()
	