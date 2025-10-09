#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 11:53:23 2025

@author: erinvanscoy
"""

# Notes for ProblemSet2 
#1a) Pull from random library, use code that defines a specific mean and SD - normalvariate

import random as rand 
 
ValueList = []

# Code for  -  For loop, which runs through all items in a range in this case (1-100)
for i in range(100): #Starting the for loop with a range of 100 values
     Val = rand.normalvariate(0.7,0.2) #Create a variable (Val) and ran random lybrary code normalvariate to specify the given mean and SD
     ValueList.append(Val) #Appending the data to my empty list
print(ValueList) #Printing all the values appended in my list 

len(ValueList) #Tells you how many items are in your list 

#B)

import numpy as np #importing from numpy library 

def funkyfunc (value):## making a function, named funkyfunc
   mean = np.mean(value) #naming np.mean as mean
   std = np.std(value) #naming tge np.std as std 
   upperlimit = mean + std * 2.5 
   lowerlimit = mean - std * 2.5
   return lowerlimit, upperlimit ## checking to see if the code is working so far
#need to return to see any function, but can only return what in your function 

funkyfunc(ValueList) #checking to see if my function worked 

#buildin on my function to include the if statment and for loop

def funkyfunc (value): #defining a new function, taking information from a value (in this case the entire list, mylist of values)
   mean = np.mean(value) 
   std = np.std(value)
   upperlimit = mean + std * 2.5
   lowerlimit = mean - std * 2.5
   keep = [] #creating a new empty list called keep
   outlier = [] #creating a new empty list called outliers
   for i in value: #combining a for and an if statment, its saying for every individual value in the list
      if i >= upperlimit: # if the value is greater than or equal too upperlimit 
          outlier.append (i) #append into the outlier list
      elif i <= lowerlimit: # if the value is less than or equal to lowerlimit 
          outlier.append (i) #append into the outlier list
      else: #ending the if statment, and saying all other values 
          keep.append(i) #all remaining values append into the keep list
   return keep, outlier #return the values from both the keep and outlier lists 
          
      funkyfunc(ValueList) #checking to see if the function works - it did!
     
 import statistics 
 
     
#Building on my function to become a while loop with recursively - not finished start here

 def funkyfunc (value): #defining a new function, taking information from a value (in this case the entire list, mylist of values)
   mean = np.mean(value) 
   std = np.std(value)
   upperlimit = mean + std * 2.5
   lowerlimit = mean - std * 2.5
   keep = [] #creating a new empty list called keep
   outlier = [] #creating a new empty list called outliers
   outliertrack = [] #creating a new empty list to track outliers
   while True: #combining a for and an if statment, its saying for every individual value in the list
      if i >= upperlimit: # if the value is greater than or equal too upperlimit 
          outliertrack.append (i) #append into the outlier list
      elif i <= lowerlimit: # if the value is less than or equal to lowerlimit 
          outliertrack.append (i) #append into the outlier list
      else: #ending the if statment, and saying all other values 
          keep.append(i) #all remaining values append into the keep list
   return keep, outliertrack #return the values from both the keep and outlier lists 


 def funkyfunc (value): #defining a new function, taking information from a value (in this case the entire list, mylist of values)
   mean = np.mean(value) 
   std = np.std(value)
   upperlimit = mean + std * 2.5
   lowerlimit = mean - std * 2.5
   keep = [] #creating a new empty list called keep
   outlier = [] #creating a new empty list called outliers
   outliertrack = [] #
   while 

##This is how AI told me to do it, the code does work and efficiently 

def remove_outliers(value):
    
    cleaned = value [:] #Making a copy of the list so its not modified directly 
    #While loop is saying to keep removing outliers until no more can be found 
    while True:
        if len(cleaned) < 2: #Cannot compute the SD with fewer than two variables 
            break 
        
        mean = np.mean(cleaned) #Calculating the mean and SD of current list using numpy
        std = np.std(cleaned) 
        
        if std ==0: #All values are the same, since the SD is 0 - no outliers possible here
            break
        #print current statsitcics and list length 
        print(f"\nCurrent list length: {len(cleaned)}")
        print(f"Original list: {cleaned}")
        
        #create a new list with only values within 2.5 SD from the mean. This than filters out the outliers
        new_list = [x for x in cleaned if abs(x - mean) <= 2.5 * std]
        
        print (f"After removing outliers: {new_list}")
        
        #Count how many values were removed in this iteration
        removed_count = len(cleaned) - len(new_list)
        print(f"Removed {removed_count} outlier(s)")
       
        #No values were removed, stio the loop, no more outliers
        if removed_count == 0:
            break
        
        #Update the new cleaned list and repeat the loop
        cleaned = new_list
        #Print the final result after all outliers were removed 
        print(f"\nFinal list length: {len(cleaned)}")
        return cleaned, mean, std


remove_outliers(ValueList)


#2 a) Hypothetical lists of student names and grades

Studentnames =["Erin","Jen", "Tom", "Ron", "Adam", "Sarah", "Lilly", "Bubs", "Garry", "Barb"]

print (Studentnames)

Grades =[76, 77, 79, 87, 88, 90, 78, 94, 99, 96]

print (Grades)

#2b) 

Gradetostudent = [] 

for grade, name in zip(Grades, Studentnames):
    if grade >= 90:
        print ("A+ " + name)
        Gradetostudent.append(grade)
    elif grade >= 85 and grade <90:
        print ("A " + name)
        Gradetostudent.append(grade)
    elif grade >= 80 and grade <85:
        print ("A- " + name)
        Gradetostudent.append(grade)
    else:
        print ("B+ " + name)
        Gradetostudent.append(grade)

##This code works, is a double for loop that goes through both lists and follows the if statment and then appends it##

print(Gradetostudent)

##Editing code to see if I can append all aspects beyond grade 



def gradeLookup (Value):
    Gradetostud = [] 
    
    for grade, name in zip(Grades, Studentnames):
        if grade > 90:
            print ("A+ " + name)
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("A+")
        elif grade >= 85 and grade <90:
            print ("A " + name)
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("A")
        elif grade >= 80 and grade <85:
            print ("A- " + name)
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("A-")
        else:
            print ("B+ " + name)
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("B+")

print(Gradetostud)
##edits to code 
Gradetostud = [] 
def gradeLookup(value):
    
    for grade, name in zip(Grades, Studentnames):
        if grade > 90:
            print (grade, name +"A+ ")
            Gradetostud.append(grade) 
            Gradetostud.append(name)
            Gradetostud.append("A+" )
        elif grade >= 85 and grade <90:
            print (grade, name +"A ")
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("A ")
        elif grade >= 80 and grade <85:
            print (grade, name + "A- ")
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("A- ")
        else:
            print (grade, name + "B+ ")
            Gradetostud.append(grade)
            Gradetostud.append(name)
            Gradetostud.append("B+ ")

print(Gradetostud)


def gradeLookup(name):
    name = input("Enter students name ")
    
    if name == "Erin":
        gradeDet = "B+ " + "76 " + "Erin "
    elif name == "Jen":
        gradeDet = "B+ " + "77 " + "Jen "
    elif name == "Tom":
        gradeDet = "B+ " + "79 " + "Tom "
    elif name == "Ron":
        gradeDet = "A " + "87 " + "Ron "
    elif name == "Adam":
        gradeDet = "A " + "88 " + "Adam "
    elif name == "Sarah":
        gradeDet = "A+ " + "90 " + "Sarah "
    elif name == "Lilly":
        gradeDet = "B+ " + "78 " + "Lilly "
    elif name == "Bubs":
        gradeDet = "A+ " + "94 " + "Bubs "
    elif name == "Garry":
        gradeDet = "A+ " + "99 " + "Garry "
    elif name == "Barb":
        gradeDet = "A+ " + "96 " + "Barb "
    return gradeDet

gradeLookup1(name) #Run this and input a name to get the corresponding data, make sure when you use function you inster name like this "Bubs"

###This is the second way Q3 was done 
##This example is pulling from the actual lists and indexing 

def gradeLookup2(grade, namelist): ##Arguments - placeholders for anythhing you want (in this case two lists )
    name = input ("Enter student name ") #user input, the user has to input something and the function will then fun through the if/for loop and the result will appear
    if name not in namelist:
       letter =  print("Student name not found") #Making everything return and print out command equal to letter,so that when return letter all critiera can be returned if plausible 

   
    if grade >= str(90):
        letter = "A+ " + namelist + "  " +  str(grade) #Have to convert the interval (grades - this list is numbers) to a string in order for them to return together as strings (text)
    elif grade >= str(85) and grade <str(90):
        letter = "A " + namelist + "  " +  str(grade) #Adding the + " " gives a space when it returns 
    elif grade >= str(80) and grade <str(85):
        letter = "A- "+ namelist + "  " +  str(grade)
    else: 
        letter = "B+ " + namelist + "  " +  str(grade)
    return letter
#use [indexed number] to index something 
#calling Erin name and grade, 
gradelookup2(Grades[0], Studentnames[0]) #Everytime you want to index something, youselect the variable or list and tell it which placeholder to take

gradelookup(Grades[0], Studentnames[0])

##edited version - had to end the loop with if name is not in namelist print "" because everything was equal to letter 

gradelookup(Grades[0], Studentnames[0])
def gradeLookup2(grade, namelist): ##Arguments - placeholders for anythhing you want (in this case two lists )
    name = input ("Enter student name ") #user input, the user has to input something and the function will then fun through the if/for loop and the result will appear
    if name not in namelist:
       letter =  print("Student name not found") #Making everything return and print out command equal to letter,so that when return letter all critiera can be returned if plausible 

   
    if grade >= str(90):
        letter = "A+ " + namelist + "  " +  str(grade) #Here I am specifiying the detail on allocating which grade (from grade list) will recieve which letter grade. 
    elif grade >= str(85) and grade <str(90): 
        letter = "A " + namelist + "  " +  str(grade) #I am then seeting up letter as the varible in which all of this information is equal to so that I can return it.
    elif grade >= str(80) and grade <str(85): 
        letter = "A- "+ namelist + "  " +  str(grade)
    elif grade >= str(76) and grade <str(80):
        letter = "B+ " + namelist + "  " +  str(grade) 
    else: 
            name not in namelist
            letter =  print("Student name not found")      
        
    return letter #

#float is a interval with decimal points 
   

#Q4)

class PersonalityProfile: #Class for personality profile
def __init__(self, participantnumb, openness, conscientiousness, agreeableness, extraversion, neuroticism)):
    self.participantnumb = participantnumb
    self.openness = openness
    self.conscientiousness = conscientiousness
    self.agreeableness = agreeableness
    self.extraversion = extraversion
    self.neuroticism = neuroticism

def a_introvert(self):
    return self.extraversion < 3

def a_openness(self):
    return self.openness >=3

def a_conc(self):
    return self.conscientiousness >=3

def a_agree(self):
    return self.agreeableness >=3

def a_neuot(self):
    return self.neuroticism >=3

    
    
class PersonalityProfile: #Class for personality profile

    def __init__(self, participantnumb, openness, conscientiousness, agreeableness, extraversion, neuroticism): 
        self.participantnumb = participantnumb
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.agreeableness = agreeableness
        self.extraversion = extraversion
        self.neuroticism = neuroticism
      
    def is_introvert(self):
        if self.extraversion <3:
            print ("True")
        else:
            print ("False")
            
        self.extraversion = self.extraversion < 3
    
    def is_closedness(self):
        self.openness = self.openness <= 3    
    
    def is_lowconscientiourness(self):
        self.conscientiousness = self.conscientiousness <=3 
    
    def is_lowagreeableness(self):
        self.agreeableness = self.agreeableness <=3
    
    def is_lowneuroticism(self):
        self.neuroticism = self.neuroticism <=3
    
    def __str__(self):
        return (f"Participant {self.participantnumb},- "
                f"Openness: {self.openness},"
                f"Conscientiousness: {self.conscientiousness},"
                f"Agreeableness: {self.agreeableness},"
                f"Extraversion: {self.extraversion},"
                f"Neuroticism: {self.neuroticism}")
##Updated version to answer question 4
        
Person1 = [0,2,1,3]
print (Person1)

class PersonalityProfile: #Class for personality profile

    def __init__(self, participantnumb, openness, conscientiousness, agreeableness, extraversion, neuroticism): 
        self.participantnumb = participantnumb
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.agreeableness = agreeableness
        self.extraversion = extraversion
        self.neuroticism = neuroticism
      
    def is_introvert(self):
        if self.extraversion <3:
            print ("True")
        else:
            print ("False")
            

Person1 = [2,3,3,1]

Person1.is_introvert 


PersonalityProfile(Person1[], Openness, conscientiousness, agreeableness, extraversion, neuroticism)

Person1 = PersonalityProfile(2, 3 , 5, 4 , 2, 3) ##Putting the personality scores in the right place, as corrsponding to their fake data

Person1.is_introvert() ##Calling to see what person 1 is, which the only def i have is on extraversion so only it will come up 





##Class can be known as a folder, used to store objects. ##Folder cabinet 
##Methods need to have variable (trying to use it on dot the method)



