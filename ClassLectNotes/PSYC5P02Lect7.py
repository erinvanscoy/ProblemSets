#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 14:42:28 2025

@author: erinvanscoy
"""

#PSYC 5P02 Lecture 7 Handling Data 

# Tuples - unchangable (fixed set of corrdinates) 
x, y = [(1,0), (0,1), (1,0), (1,0)]
type 

coards = [(1,1), (2,2,), (3,3), (4,4)]

# Dictionaries - Pairing things and using one as a key (in this case the place is the key)
nbaTeams= = {'Los Angeles': 'Lakers': 'Toronto': 'Raptors': 'Chicago': "Bulls"}

#Not indexed by location(which lists are)
#Dictionaries are indexed by keys - 
#first item it the key and second item is the value 
#Retreive the dictionary by calling the key [e.g., ['Toronto']] or by doing nbaTeams.get("Toronto")


#Numpy 
import numpy as np 

#To creat an array, you need to call the array method 
arr = np.array([1,2,3,4,5]) #size 5,0

mdArr = np.array([[1,2,3], [4,5,6], [7,8,9]]) #round brackets start function, first set of square brackets is defining array, if it must be 2nd array need 2 square brackets
#Size 3,3

print(mdArr) #It will print out as a nice array of sections

Array3d = ([[[0,0,0],[0,0,0]], [[1,2,2]],[0,2,9]]) #Making a 3x3 array. 3 rows and 3 columns 

mdArr[1] #indexing the second element in the array


mdArr[0,1] #Indexing to the - First row second column 


for x in mdArr: #Turning it into a one dimensional list, taking each () as a value 
    print(x) #Going through the triplts 
    

for x in mdArr: #Turning it into a one dimensional list, taking each () as a value 
    #print(x)
    for y in x: #For everyvalue in the triplets go loop through them. Goes through each value independelty in the triplets 
        print(y)


for x in mdArr: #Turning it into a one dimensional list, taking each () as a value 
    #print(x)
    for y in x: #For everyvalue in the triplets go loop through them. Goes through each value independelty in the triplets 
        print(y)
        print(x) #Will list through y (1; each first element in the triplet) first, and then x(1,2,3) - the triplets

#Indexing and masking 

newArr = [5,6,3,4,5,6,7,2,3]

newArr = np.array(newArr) #turn list into a numpy array 

#Creat a mask where data is greater than 2 
mask = newArr > 2

newArr[mask]#using new mask - return the data if this is true 

cleanData = newArr[mask] #Can set a new varible to be store the new data in (using the mask we made)

cleanData = newArr[newArr > 2] #Can also just do the boolion inside of the object

newArr2 =[0,1,2,3,4,5,6,7,8]

newArr2 = np.array(newArr2)

x = newArr[newArr2 > 4] #If you wanted trials after trial 4 for e.g., then you could use this and store it into an object 

cleanedData = rt((cond ==1) and ()) #This is what you would use many times if you need to combine different aspects of experiment to see if its true/false

#Importing data 
data = np.loadtxt(fname='inflammation-01.csv',delimiter= ;'',)

print(data[0:4,0:10]) #The collon will index everything in that dimension 

data[0,5:-1] #end is -1 and start is 0 


x = data[0:1,0:1] #Second number in the range will be one past what you are looking to get 

meanVal = np.mean(data) #Compute overall mean 

print(meanVal)

meanVal = np.mean(data,0) #Computes the mean by specifiyig individual axis 
print(meanVal)

data[0] #This will show data from one row 

np.mean(data[0,:]) #0 specific row  and : by all the columns (: is saying take all the elements from the rows or columns)
np.mean(data[:,0]) #This is opposite - take all rows, by 0 column 

import random 


random.randint #generates a random integer from 0-100 
random.randint(100) #Generates a random number within 0-100
randData = random.randint(100, 110,size =[10,50]) 
random.rand()
random.choice(data[0:1]) #Takes a random value (coordinates/conditions)



conds = [1,2,4]
random.shuffule(conds) #will not make the original object the same 
random.permutation(conds) #Shuffules but leaves the original values the same 

#Simulate data that follows a normative distribution - useful when simulating data 
#Create customize distribution (numpy) 

#Panadas
#Set up to deal with text data slightly better. Can handle muiltiple different types of data 

#Two different main types of structures: - series, and dataframe 

import pandas as pd
pd.series(['4, cups', '1 cup', '2 large', '1 can']) #Same as a numpy array 


pd.series(data = ['4 cups', '1 cup', '2 large', '1 can']) #Inputing data as a series 
vol = pd.series(data = ['4, cups', '1 cup', '2 large', '1 can']) 

s = pd.series(data=(1,"2",3,"4") #can input both strings and int in the series
s.astype('int') #will return all the numbers as an int type, can convert all things into an int and then can comput mean/sd etc 
# If in decimals, would want to do s.astype('float'), and 'str'


data = pd.series([1,2,pd.NA,4,4]) #Will show as NA (missing data)

data.dropna(inplace=True) #No longer has missing values (NA)


data.fillna('Null', inplace = True) #This will replace NA will Null 


data.apply(np.sqrt)  #Data.apply is going to apply the method we are calling, pd.na would work (consdiered an int) but because we changed it to Null (str) this wouldnt work but it will on a list of int


data.apply(lambda x: x + 1) #Specifying our own function, at the value of x add 1 
#Useful for transforming data and stimulating data 

data = pd.read_csv('RTdata.csv') #Imports data onto the application and opens it up into a data frame 
#First row as labels 



data['subjs'] #Gives all the rows from that column 

data['subjs'][5] #How to index from one column and one value in that row 

data.index_col

data = pd.read_csv('RTdata.csv', index_col='subjs') #This is how you start the indexing onto subjects (which is the first column)

data.iloc[2,5] #iloc - Giving it the range to index
data.loc[:,'K'] #loc - Index using names (from colm) and loc method 
#Takes everything from column K 
data[:]['K'] #This is another way to do this (works)

#Getting RT for only males 
data.groupby('sex').mean() #This will sort the data based on grops (F,M) and then calculate the mean for each group 

output = data.groupby #Saving the mean RTs and other data based on sex into a new object (output)
output.loc['m']['RT'] #Putting or indexing the male mean RT from output object 
        
data.groupby(['sex','race']).mean() #Seperate all data based on race, and sex - can then again put into new object 

help(np.mean)

#Manipulating textual data 

titanic["Name"].str.lower()

import pandas as pd

titianic = pd.read_csv ("titanic.csv")

titanic['Name'].str.lower() #Converted the upper and lower case text to lower case text 

titanic['Name'].str.split(',') #Splits the data (the names with a coma )
 
titanic["Surname"] = titanic["Name"].str.split(',') #Keept name the same but then split up the name and moved the last name into a surname column 




            
