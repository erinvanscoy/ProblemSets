#Exam Question 6
#Erin Vanscoy

#Importing all needed libraries 
from psychopy import visual, event, core, data, gui #Importing all needed functions from psychopy

win = visual.Window([1000,1000], fullscr=False, units = 'pix') #Creating a window that displays at 1000x1000, and it in units pix 

trial = []

import numpy

#First I am creating the stim I will need to create this experiment. That being the fixation cross, visual GO text and my key response.

fixation = visual.TextStim( #Creating a fixation cross that will display for 1 second in the trial 
    win,  #setting it to display on my main window 
    pos=(0, 0), #setting it to be positioned in the center 
    text ="+", #having the text set as a "+" fixation cross 
    color = "white", #setting the colour to white
    height = 60) #setting the height to 60 

#creating the text that will go into my stim
textS = ("GO!")

#Here I am creating My textStim that I will use in the trial experiment 
textStim = visual.TextStim(win, text=textS, pos=(0,0),color='white', height=60)

#Next I have decided to use a while loop since this is only a 1 trial experiment, this will make sure it does not end until the conditions are meet (pressing a key to end the experiment) 

response=[] #empty list to store my 

while True:
    
    fixation.draw() #Drawing the fixation visual "+" to prepare it to be flipped onto the windows screen
    win.flip()  #Flippng the stimulas to the main window.
    core.wait(1) #Allowing the fixation prompt to stay on the screen for .5 seconds. 
    
    textStim.draw() #drawing the textstim to the scren
    win.flip() #flipping it to the main window 
    
    respClock = core.Clock() #Start a new clock here
    respClock.reset() #Reset the clock to 0.00 seconds
         
         
    resp = event.waitKeys(keyList = ["space", "escape"], timeStamped = respClock) ##setting varible resp to my keylist and making it timestapmed to the respClock
    RT = respClock.getTime() ##Setting a varible name (RT) to my clock. 
    print(RT) #Here I am printing the RT from the keypress response 
   
    if resp: #Checking if a key was pressed for this trial
        resp, RT = response[0] #Gets the key and RT from the response and stores it into response list together for later (if needed)
        
        if resp == "escape": #If the participant presses escape, exit the experiment and close the program
            win.close() #Close the window and quit ending the loop 
            core.quit()






