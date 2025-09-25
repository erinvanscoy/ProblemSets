# -*- coding: utf-8 -*-

# Lecture4.py
#Erin Vanscoy

"""
Spyder Editor

This is lecture 1 scipt file 
"""

#This is a comment 

myVar = "hello world" #writing hello world to myVar

#Loops - a fundamental and powerful concept that is an instruction that repeats until a specifed condition is met 
# A for loop - loop that runs for a present number of times
# A while loop - repeated as long as an expression is true 

#These are for loops

for i in range(1,5): 
    print ("I am in the loop")
    print(i)
    
print ("I am out of the loop")

# I is being assigned a value 1 - 5 and the only thing excuted is the indented values 
# Prints out the range 1-4, but remember the range is exclusive 
# As soon as you step outside with a nonindented line, the statment is finished


for i in range(1,5): 
   print ("I am in the loop")
print(i)
print ("what is this")
    
print ("I am out of the loop")

# why did it print 4 - because I is equal to 4 look at the varible name and values 

#Here is a new loop

mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)


mylist = ["apple", "banana", "cherry"]
for x in range(len(mylist)):
    print(x)

# Turned list into numeric values (0-3). 

#These are while loops 

i = 1
while i < 6:
    print(i)
    i+=1

# += means take the current value of the varible on the left and than add to it whatever is on the right

# control c in counsole terminal - if you get stuck in an infinite loop 

# the break command - a conditional effect , the break command will exit out of the loop entirley 
# continue command - skils the remaining commands in the loop and move on to the next loop iteration 

i = 0
while i < 6:
    i +=1
    if i == 3:
        continue
    print (i)
    
#printed 1-6 but took out 3. Saying fastforward to the next iteration of the loop 

#scope of a varible - scope referrs to region of the code in which a varible/resource is visable and accessible 


#in-class exercise code 

for i in range(0,5):
    x = i
    print(x) 
    
print (i)
print (x)


#new varible i that has a range 0-5 

#Python Libraries - importing functions from specific libraries 

#Common library used - random library method (randomizing stimuli, conditions, time etc)

#random seed - seeded the random number generator to 1 (can do this with participant code to track information)
#random randint - randomly assignes number from the range you give 

#functions - used to increase efficiency of the code, repeates blocks of code 

# ends in a : and everything after has to be indented 

def nameprintfunc(name):
    print ('The name is ' + name)
    return name 
    

def adderfunc(val):
    x = val1 + val2
    print(x)
    
# You have to return x 

def adderfunc(val):
    x = val1 + val2
    print(x)
    return x 



def adderfunc(val1, val2 = 4):
    x = val1 + val2
    return x 

#returning two varibles (x,y) and adding a help function for the new function

def adderfunc(val1, val2 = 4):
    """Adds two numbers together 
    
    """
    
    x = val1 + val2
    y = (val1 +val2) + 2
    return x, y

#Classes are ways to combine functions and data
#A way to build flexibility into the coding 

#class example code below 


class car: #definition of a class 

    def __init__(self,color = 'white'): #initialize attributes of every instance of the class
        self.speed = 0 #self allows you to access varible from anywhere else in class
        self.color = color #colour is defined by (optional1) input
        
    def drive(self):
            self.speed += self.speed + 1
            
    def breaking(self):
        self.speed=self.speed +-1 



    
