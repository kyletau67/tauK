#Portends Greatness -- Michelle Tang and Kyle Tau
#SoftDev1 pd 6
#K06 -- StI/O: Divine your Destiny!
#2018-09-13

import csv
import random

file  = open("occupations.csv", "r") #open and read the file
occupations = file.readlines() #lines of the file are put into the list, occupations
file.close() #close the file since we no longer need it

dictionary = {} #initialize dictionary!
for item in occupations[1:len(occupations)-1]: #add occupation into dictionary, skipping the first line (headers) and the last line (total)
  key = item[:item.rfind(",")] #returns the occupation 
  value = float(item[item.rfind(",")+1:item.rfind("\\")]) #returns the percent corresponding with that application
  dictionary[key] = value  #input key and value into the dictionary

#Pre-condition: Assumes a csv file has been processed and made into a dictionary
#Post-condition: Returns an occupation where the results are weighted by the percentage given
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

print (randOcc())