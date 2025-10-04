# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
###ProbelmSet2
#Erin Vanscoy 2025/10/02

#1a) Imported normalvariate function from random library and appended the information in ValueList.

import random 

import random as rand 
 
ValueList = []

#My Code for a For loop, which runs through all items in a range in this case (1-100)

for i in range(100): #Starting the for loop with a range of 100 values
     Val = rand.normalvariate(0.7,0.2) #Create a variable (Val) that equals the random library normalvariate function and specifies the given mean and SD
     ValueList.append(Val) #Appending the data to my empty list
print(ValueList) #Printing all the values appended in my list 

#1b) Creating a function that calculates the mean and standard deviation and removes values that exceed 2.5 SD

import numpy as np #importing from numpy library 

def funkyfunc (value): #defining a new function, taking information from a value (in this case the entire list, mylist of values)
   mean = np.mean(value) 
   std = np.std(value)
   upperlimit = mean + std * 2.5
   lowerlimit = mean - std * 2.5
   keep = [] #creating a new empty list called keep
   outlier = [] #creating a new empty list called outliers
   for i in value: #combining a for and an if statement, its saying for every individual value in the list
      if i >= upperlimit: # if the value is greater than or equal too upperlimit 
          outlier.append (i) #append into the outlier list
      elif i <= lowerlimit: # if the value is less than or equal to lowerlimit 
          outlier.append (i) #append into the outlier list
      else: #ending the if statement, and saying all other values 
          keep.append(i) #all remaining values append into the keep list
   return keep, outlier #return the values from both the keep and outlier lists 
          
funkyfunc(ValueList) #checking to see if the function works - it did!

      
#1b) Building on my function so that it recursively removes outliers. For this question I did require AI assistance, I was having a really difficult time getting the code to continue removing outliers after one round. 
##This code helped me to figure out how to generate a while loop that continiously removes outliers until there is no longer any and break the loop based on the SD parameters. 

def remove_outliers(value): #Making a new function to try and remove outliers recursively
    
    cleaned = value [:] #Making a copy of the list so its not modified directly 
    
    #While loop is saying to keep removing outliers until no more can be found in the given list
    while True:
        if len(cleaned) < 2: #Cannot compute the SD with fewer than two variables 
            break 
        mean = np.mean(cleaned) #Calculating the mean and SD of current list using numpy
        std = np.std(cleaned) 
        if std ==0: #All values are the same if SD = 0, meaning that no outliers possible here
            break
        #print current stats and list length 
        print(f"\nCurrent list length: {len(cleaned)}")
        print(f"Original list: {cleaned}")
        #create a new list with only values within 2.5 SD from the mean. This than filters out the outliers
        new_list = [x for x in cleaned if abs(x - mean) <= 2.5 * std]
        print (f"After removing outliers: {new_list}")
        #Count how many values were removed in this iteration
        removed_count = len(cleaned) - len(new_list)
        print(f"Removed {removed_count} outlier(s)")
       #No values were removed, stop the loop, no more outliers
        if removed_count == 0:
            break
        #Update the new cleaned list and repeat the loop until break
        cleaned = new_list
        #Print the final result after all outliers were removed 
        print(f"\nFinal list length: {len(cleaned)}")
        return cleaned, mean, std #returning the new list, mean, and SD

##1c)Calling up both the functions I made to remove outliers below. This code removed one outlier. The new mean = 0.662, while the SD = 0.192.
    
    unkyfunc(ValueList) 
    remove_outliers(ValueList)


#2a) Hypothetical lists of student names and grades

Studentnames =["Erin","Jen", "Tom", "Ron", "Adam", "Sarah", "Lilly", "Bubs", "Garry", "Barb"]

print (Studentnames)

Grades =["76", "77", "79", "87", "88", "90", "78", "94", "99", "96"]

print (Grades)   

#2b) This is my code for combining both lists with a for loop and if statement 
##This code is going through both lists of data (Grades and Studentnames). 
# The if statement is setting parameters to sink up both lists based on grade and student name.


for grade, name in zip(Grades, Studentnames):#This is a for loop that is taken from two lists (grades and student names)
    if grade >= 90: #Here I am setting the first parameter of the if statement, if the grade is greater than 90 print an A+ and the name corresponding to the grade.
        print ("A+ " + name)
    elif grade >= 85 and grade <90:#Here I am specifying the next parameters, if grade is greater than or equal to 85 and less then 90 print A and the corresponding name to the grade.
        print ("A " + name)#
    elif grade >= 80 and grade <85:#Here is the next parameters, in which if the grade is greater than or equal to 80 and less than 85 print A- and the corressponding name to the grade.
        print ("A- " + name)
    else:
        print ("B+ " + name) #This is the last paraemter, its saying all the rest of the data points, print under B+ with the corresponding name. 
      

#3a)

#I have created a function (gradelookup) that asks you to input student names, I then made an If statement to identify the parameters associated with each name.

def gradeLookup(name):
    name = input("Enter students name ") #Input student name to get detail 
    if name == "Erin": #Telling the function the name parameters
        gradeDet = "B+ " + "76% " + "Erin " #Giving the grade detail of that student 
    elif name == "Jen":
        gradeDet = "B+ " + "77% " + "Jen "
    elif name == "Tom":
        gradeDet = "B+ " + "79% " + "Tom "
    elif name == "Ron":
        gradeDet = "A " + "87% " + "Ron "
    elif name == "Adam":
        gradeDet = "A " + "88% " + "Adam "
    elif name == "Sarah":
        gradeDet = "A+ " + "90% " + "Sarah "
    elif name == "Lilly":
        gradeDet = "B+ " + "78% " + "Lilly "
    elif name == "Bubs":
        gradeDet = "A+ " + "94% " + "Bubs "
    elif name == "Garry":
        gradeDet = "A+ " + "99% " + "Garry "
    elif name == "Barb":
        gradeDet = "A+ " + "96% " + "Barb "
    return gradeDet #return the grade detail inputted based on the user inputted name 

gradeLookup(name) #Run the function and insert a name with ("") to get the corresponding data 

##3b) This is the second way I found to answer this question. Here I again created a function that takes user input after you put in two lists with an index spot, in this case student grades and student name list.
##For example you insert the index of the data you want (gradeLookup2(Grades[0], Studentnames[0]), then it will ask you to clarify the students name. In this case you would insert Erin. Then the data will appear. 

def gradeLookup2(grade, namelist): ##Arguments - placeholders for anything you want (in this case two lists )
    name = input ("Enter student name ") #user input, the user has to input something and the function will then fun through the if/for loop and the result will appear
    if name not in namelist:
       letter =  print("Student name not found") #Making everything return and print out command equal to letter,so that when return letter all criteria can be returned if plausible 

   
    if grade >= str(90):
        letter = "A+ " + namelist + "  " +  str(grade) #Here I am specifying the detail on allocating which grade (from grade list) will receive which letter grade. 
    elif grade >= str(85) and grade <str(90): 
        letter = "A " + namelist + "  " +  str(grade) #I am then setting up letter as the variable in which all of this information is equal to so that I can return it.
    elif grade >= str(80) and grade <str(85): 
        letter = "A- "+ namelist + "  " +  str(grade)
    elif grade >= str(76) and grade <str(80):
        letter = "B+ " + namelist + "  " +  str(grade) 
    else: 
            name not in namelist
            letter =  print("Student name not found")      
        
    return letter #I am returning letter which will have the correct data based on parameters of the if statement. 

#calling Erin name and grade here by indexing 0 
gradelookup(Grades[0], Studentnames[0]) 


#3Bonus) Doing it either way can be beneficial and allows for direct access to the specific elements within the lists. However, using this second method allows for the user to insert new lists rather than only the set information. 
#Thus, the second method I did is a more efficient way to get information from any two lists.

#Q4)Making a class for personality profile cases and creating a function to pull up results. 
      
    class PersonalityProfile: #Class for personality profile

        def __init__(self, participantnumb, openness, conscientiousness, agreeableness, extraversion, neuroticism): #Defining my class here, using the init method to allocate values to objects (in this case the big five personality traits).
            self.participantnumb = participantnumb #Setting up all my objects to be instance variables (unique to each object I created in this class)
            self.openness = openness
            self.conscientiousness = conscientiousness
            self.agreeableness = agreeableness
            self.extraversion = extraversion
            self.neuroticism = neuroticism
          
        def is_introvert(self): #defining a function within the class, in which the user can access the instances (in this case extraversion score)
            if self.extraversion <3: #Setting up an if statement to assign parameters for extraversion scores. 
                print ("True") 
            else:
                print ("False")
                

    Person1 = PersonalityProfile(2, 3 , 5, 4 , 2, 3) ##Putting the personality scores for fake person (person 1) in the right place, as corresponding to their fake data and the class set up.

    Person1.is_introvert() ##Calling the function within the class to see if person1 is high on the extraversion scale and considered an extrovert. 
    ##Could do this for all the big five items if I continued on and created each function within the class. 

