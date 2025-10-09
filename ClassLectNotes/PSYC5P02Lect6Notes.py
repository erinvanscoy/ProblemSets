#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:34:45 2025

@author: erinvanscoy
"""

## PSYC 5P02 Lecture 6 Review Notes 



##Going through the assignment 
##Canc create a flow chart to represent what you want your code to do 


##Question 1
##Stats function does not allow you to generate hundreds of different code but Numpy does 
##To generate a list of numbers - Var = [] building in a loop what the value is - generating a loop but can do the entire thing witin a variable 

##Start with importing any nessesary library (numpy) -- calculate mean and sd --- define outlier limits (upper and lower limits) - find all outliers - check if their are more outliers - if no  break if yes continue back in the look at calc mean and sd of new data

##Remove outliers using a loop -- first way to do this
import random
import statistics

data = [random.normalvariate(0.7,0.2) for i in range(100)] #creating a list of values 
threshold = 2.5 #cuttoff threshold 

mean = statistics.mean(data) #calc mean from library
SD = statistics.stdev(data) #calc sd from imported library 

upperlimit = mean + threshold * SD #calc limits 
lowerlimit = mean - threshold * SD


cleaneddata = [value for value in data if upperlimit <= value >= lowerlimit]
##for the entire list of data if its within these limits then output it to the the newcleaned data 
##lopping through the list, if the condition is true then append it to the cleaned data list


##Remove outliers in numpy slicing -- second way to do this 
import numpy as np 

data = [random.normalvariate(0.7,0.2) for i in range(100)] #creating a list of values 
threshold = 2.5 #cuttoff threshold 

mean = statistics.mean(data) #calc mean from library
SD = statistics.stdev(data) #calc sd from imported library 

data = np.array(data)

upperlimit = mean + threshold * SD #calc limits 
lowerlimit = mean - threshold * SD


cleaneddata = data [(data < upperlimit) & (data > lowerlimit)]
##Data is the original list, taking from the original data and checking the upper and lower limits 

#If the values are true then it will append it all at once into the cleaned data list
##(looking at the whole array all at once)
##This way is preferable because loops take longer - if you can slice instead of using a loop then slice!



## if len(cleaneddata) == len(data): 
#   break 

#Creating the while loop

cleaneddata = []

def trimmMeans (data, threshold): ##whatever list of data and the threshold (2.5 cuttoff)

while true:
        
    cleaneddata = []
    
    mean = statistics.mean(data) #calc mean from library
    SD = statistics.stdev(data) #calc sd from imported library 
    
    data = np.array(data)
    
    upperlimit = mean + threshold * SD #calc limits 
    lowerlimit = mean - threshold * SD
    
    
    cleaneddata = data [(data < upperlimit) & (data > lowerlimit)]
    data = cleaneddata 
    
    IF len(cleaneddata) == len(data): #if the two of the lists are the same, then we exist the loop 
        break 
    else:
        data = cleaneddata  #if not we have to update the data to be cleaned data (based on last outlier removed) - and the loop retarts 
        
    return cleaneddata #The function and loop are local to this function, to make it global you need to return it - returning 

newData = trimmMeans (data, threshold)

##Functions we build around what we want to do - loops classes etc 


#2b) solution 
for i in range (len(names)):
    print(names[i] + ", grade: " + str(grades[i])) 
    
    
#3) Getting the input from two lists using indexing 
    
names = ["joe", "paul", "joel", "lou", "anson", "erin"]
grades = np.random.randint(71,90,6) #gives us random numbers between 71-90 (6) - of them 

names.index("joe") ##indexing where the name is in the list 

    
inputname = input ("please enter a name:")
idx = names.index(inputname)
print(names[idx] + "s grade is:" + str(grades[idx])) ##in the list names, take out the index number from where that name is, and add the text, and then pull the grades (second list) from the same index number

##from variable names, find the location where names is equal the input name, then using that to find the location of the second variable using indexing 

    
##Additional note 
all = [["joe", 88], ["paul", 80]]
all [0][1] ##how to index one item in a muilitvariable list, 0 is indexing alyssa and 1 is indexing the grade 
    
    


    