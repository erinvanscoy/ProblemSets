#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 15:28:17 2025

@author: erinvanscoy
"""
import numpy as np


##Question 5 - creating a class 
class Participant: #Here I am defining my class as participant
#Part 1 - Assigning what the object will hold 
    def __init__(self, participantID, InitialRTs, trials): #__init is a special method that runs when you create a new object. The user will input the participant ID,inital RTs and number of trials.
        self.participantID = participantID #stores the ID passed through as part of the object
        self.InitialRTs=InitialRTs #stores the inital RTs as part of the object
        self.trials= trials #stores number of trials or specific trial number (either way behind using this class)
        
    def MeanRT(self, meanRT): #first method creating a mean of my RTs
        self.InitialRTsT=  np.sum(meanRT)/ len(meanRT) #Sum of the mean RT / but the length of values in the list will give the mean RT
        print(meanRT) #print answer 
        
    def NewRT(self, NEWRTs): #adding new RTs method 
        self.InitialRTs.append(NEWRTs) #appending the new RT value into the inital RT list 
        print(self.InitialRTs)
    
    def NumT(self,NumT): #number of trials method 
        len(self.trials) #get the length of the number of trials 
        print(self.trials) #print out lenth of trials 
    
    def summary(self):#a method to print out a summary of all results 
        print(self.participantID, self.InitialRTs, self.trials) #print summary of all responses 


SubjectS01 = Participant(participantID= 'S01', InitialRTs = [1000,1200,1400], trials = 5)  #Inputting false information for subject S01.
#Here I have inputted the participant ID, their inital RT data and the numer of trials they have completed 

SubjectS01.NewRT(1900) ##Addint a new RT into this participants RT list within the Inital RT class (folder)


SubjectS01.summary()



#Question 3 - Creating a function 

#Step 1 - import needed libraries
import random

RandomRT=[] #Here I have created an empty list that will contain fake data to check my function

for i in range(10): #creating a for loop to generate my fake numbers based on false data 
    RT=random.normalvariate(1000,500) #setting RT to hold random RTs (mean is set too 1000ms, SD = 500ms)
    RandomRT.append(RT) #appending (or moving) these data into my empty list 
    print(RandomRT) #printed the list to check it was there 


#creating my defintion 
def Summarize_rts(rt_list):  
    mean = np.mean(rt_list) #calculating the mean using numpy libraries and attaching it to a varible mean
    std =np.std(rt_list) #calculating the std using numpy libraries and attaching it to a variable std
    Tlen=len(rt_list)#Getting the length (number of trials or RTs) using the len command (length of values) and attaching it to a varible Tlen
    
    Sumofdata=[] #making a new list alled sum of data to append this information too
    
    Sumofdata.append(mean) #appending mean
    Sumofdata.append(std) #appending std
    Sumofdata.append(Tlen)#appending Tlen
    
    #printing out the mean, STD, and length of trials 
    print(f"Mean RT {mean}")
    print(f"Standard Deviation {std}")
    print(f"Length of Trials {Tlen}")
    
         

Summarize_rts(RandomRT)   ##Calling my fucntion to see if it prints out the stats - it does! 

#I did not build onto this funication to compare two lists of means, I did not have time. 


    
    
    
    
    
    
    