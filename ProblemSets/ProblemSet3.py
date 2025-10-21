##Erin Vanscoy Problem Set 3 2025/10/23

#Setting up my files so that the data will write to them automatically
#First part of this experiment I need to import components I will need from Psychopy. This being the visual, event, and core components.
from psychopy import visual, event, core, data, gui

#I also imported the random and numpy libraries
import random
import numpy as np 

#Overview - What I need to find and do:
##SetSize = which condition or setsize (6,8,10)
##TargPresent = is the target present? (yes or no; 0,1)
##RT = reaction time on responses 
##Correct = was the trial responded to correctly (yes or no)


#Using the GUI function to create a way to collect participant code and condition.
##Information on the .gui function and display set up was pulled from the PsychoPy website (https://www.psychopy.org/api/gui.html), lecture 5 material, and a online respository with PsychoPy basics titled -Experimentation l - intro to Psychopy l (https://github.com/PeerHerholz/Python_for_Psychologists_Winter2021/blob/master/lecture/experiments/intro_psychopy_I.ipynb)
#I start by creating a list/dictionary called participant info which will be used to degin what will be asked by the user
#Participant number "" - means that this input  box will be empty, allowing the user to input whatever their participant number is
#Setsize [6,8,10] -  will appear as a dropdown menu with three conditional options (setsizes of 6,8 or 10]
#Trials per condition - was set as a box with a fixed value of 8 
Participant_Info = {'Participant Number': "", "Set Size":[ '6', '8', '10'], 'Trials per condition': "8"}

#This code then creates a new display box using the GUI module
#I set it to have fields that incorperate the participant number, set sizes, and trials (experimental setup)
dlg = gui.DlgFromDict(Participant_Info, title = 'Experimental Setup') 
if not dlg.OK:
    core.quit() #If the participant closes this dialog box then the program will end

#Next I saved the participant responses (data) to new variables 
Participant_Number = Participant_Info['Participant Number'] #Remains a string 
set_size = int(Participant_Info['Set Size']) #Converted to int
numb_Trials = int(Participant_Info['Trials per condition']) #Converted to int

half_trials = numb_Trials // 2 #Here I am calculating total trials divided by 2
Trial_Condition = [1]*half_trials + [0]*(numb_Trials - half_trials) #Next I created a new variable that includes a list of trial condtions that randomize trials based on the target being present/absent 
##1 * half trials (4) - creates a list with 1 presented half times (e.g., 4 times), then 0 * numb trials (total 8) - halftrials (4) = 0 being presented 4 times 
random.shuffle(Trial_Condition) #Then I randomized the order in which these are presented 
#Random shuffle code is a way to rearrange elements in a list. I used the W3Schools website (https://www.w3schools.com/python/ref_random_shuffle.asp) and the online respository with PsychoPy basics titled -Experimentation l - intro to Psychopy l (https://github.com/PeerHerholz/Python_for_Psychologists_Winter2021/blob/master/lecture/experiments/intro_psychopy_I.ipynb).

#Next I am making my visual window. I set the window size to 1000x1000. Fullscreen = false, means that the window will not take up the entrire screen. Units were then set to pixels. 
win = visual.Window([1000,1000], fullscr=False, units = 'pix') 

#Next I am defining my target present, target absent variables. 
#If the target is present, it is associated with 1. If the target is absent it is associated with 0.
Targ_present = "1" 
Targ_absent = "0"

#Making a list of the potential orientation formats for the letters. - Relevant in my code below 
possibleOri = [0, 90, 180, 270]  

##Empty lists for my if statment bellow, in regards to calculating an average RT and Accuracy score. These lists are placeholders for participant RT and accuracy scores on each trial. 
All_RT = []
All_Acc = [] 

#Next I am defining introduction instructions so that the participant will be able to recieve information on what to do in this task. 
#I have set a variable to equal what I want these instructions to say (the instruction text). I have told the participant that they will be shown a target letter on the screen and will need to identify it. 
#I then indicated what the target letter is and how to to proceed to identify that the target letter is either present or not. 
#Participants were advised to press 1 if the target letter is present, and 0 if the target letter is not present. 
#I then give the instruction that they are to press space to continue or esc to exit the program. 
Instructions_txt = ( 
    "Welcome to a Visual Task Assessment.\n\n"
    "You will be shown a target letter on the screen with a series of distractor letters.\n\n" 
    "Please indicate if you believe a target is present on the screen useing the keyboard.\n\n"
    "The target letter for this task is T.\n\n"
    "Press 1 if you believe the target is present.\n"
    "Press 0 if you believe the target is absent. \n\n"
    "Press ESC at any time if you wish to leave the experiment.\n\n"
    "Press Space to continue.")

#Here I am assigning a varible to a visual text stim. The visual text stim is set to appear on the main window with the text I created from Instructions_txt. 
#I also applied a give n height and central positioning of the text stim. 
Instructions = visual.TextStim(
    win, 
    text = Instructions_txt,
    color = "white",
    height = 30,
    pos = (0,0),
    )

Instructions.draw() #I am now drawing the Instruction stimulas I just created. 
win.flip() #Flipping this to appear on the working window.

#Assigning a variable keys to the participants keybored responses 
#Keylist limits which keys are accepted, in this case space (continue to the study), and escape (to quit). 
keys = event.waitKeys(keyList = ["space","escape"]) 

#I then created an if statment just in case the participant decides to quit the program before starting the experiment. 
if "escape" in keys: #If the participant presses escape then the entire experiment will close
    win.close() #This closes the window 
    core.quit() #This quits the experiment

#Next I made a variable and attached them to the window I made and the png stimulas images provided for this assignment. Both images are in this directory so I can directly access them by stating the file name. 
#I then attached a size to the stimulas. Now when I call these variables (Lstim, Tstim), the L stimulas and T stimulas will appear on my window at the given size.
Lstim = visual.ImageStim(win,'L1.png', size = 60) 
Tstim = visual.ImageStim(win,'T.png', size = 60)
#Both of these images I found on an online repo and downloaded them to use in this experiment. The images are the exact same as the ones given for the assignment, however these ones had a transparent background which were easier to implement into the experiment. 
#Stim Repo - (https://github.com/colinquirk/PsychopyVisualSearch/tree/master/stim)

#Here I am making a fixation visual for the experiment. I have assigned the fixation to my main window, I assigned a central position (0,0), and for it to appear as a + symbol. I then assigned it the color white and a height of 60.
fixation = visual.TextStim(
    win, 
    pos=(0, 0), 
    text ="+", 
    color = "white", 
    height = 60)

#Here I am making different positions for the stimulas based on a clock layout format (circle)
#I used AI here to generate these random positions of the stimuli (assuming central is 0,0) so that the letters would appear on the window in a circle (clock format). 
positions =[
    (0, 250), (147, 212), (237, 75), (237, -75), (147, -212),
    (0, -250), (-147, -212), (-237, -75), (-237, 75), (-147, 212)
]

##Practice Trials 

##Next I am creating practice trials for the experiment. 
##I start by creating a variable (practice trials) - which will consists of 4 trials. I then create a variable to hold both target present(1) and target absent(0) values. There are two of each type of trials to ensure that the target is present 50% of the time. 
#I then used the random shuffle code to randomize the order in which the target absent/target present trials are in.
Pract_Trials = 4
Practice_Cond = [1]*2 + [0]*2
random.shuffle(Practice_Cond)

#Here I am then creating a text varible to consist of what will appear on the window before the pratice trials begin.
Prac_Text = (
    "Lets start with a couple Practice Trials.\n\n"
    "Press ESCAPE at any time if you wish to leave the experiment.\n\n"
    "Press SPACE to continue.")

#I then created a visual stimulas that will appear on the window, I then set the paramters to include the practice text, a centered positioning (0,0), white text, and a height of 30. 
Practise = visual.TextStim(
    win, 
    pos=(0, 0), 
    text = Prac_Text, 
    color = "white", 
    height = 30)

#Here I draw my new text stimulas so that it is created and prepared to be put on the window
Practise.draw()
win.flip() #I then flip the text stimulas onto the window, this ensures it appears to the user

#Next I use the event waitKey list function to specify what keys the participant must press if they wish to move forward or exist the program
#The keyList argument tells the system to only respond to the keys I put in the keylist. In this case that being the space and escape keys
PracKey = event.waitKeys(keyList = ["space","escape"]) 

#I then go ahead and create the practice loop (looping through four trials) in the experiment
for trials_prac in range(Pract_Trials): #Sets the parameter to repeat the loop for every pratice trial set in range (in this case 4)
    
    fixation.draw() #This draws the fixation stimuli I created earlier 
    win.flip()  #Fixation display then gets presented on the window
    core.wait(.5) #The fixation is set to be held on the screen for .5 seconds. 
    
    pres = Practice_Cond[trials_prac] #I then set pres to be equal to whether the trial has a present target or not depending on the trial number 
    
    T_pos_prac = random.randrange(set_size) if pres else None #If target is meant to be present for each trial, choose a random position for it to be in. If no target present, set the position to be None.
    #The random.randrange is used to randomly select and return an element from a list. I referenced the W3schools website again - (https://www.w3schools.com/python/ref_random_randrange.asp)
    
    for i in range(set_size): #Loop through each item, depending on the set size. Deciding what to draw at each positioning 
        if pres and i == T_pos_prac: #If the target is present and the current position is where the target should be then draw the target 
            Tstim.pos = positions[i] 
            Tstim.ori = 0 #Keep the target upright 
            Tstim.draw() #Draw the target on the screen 
        else: 
            Lstim.pos = positions[i] #Places distractor in a location
            Lstim.ori = random.choice(possibleOri) #Randomly assigns the orientation based on the given list
            Lstim.draw() #Draws the distractor on screen
            

    win.flip() #Show stimuli on screen
    
    #Setting another key response using event wait key funcion. Setting the key list to be target present (1), target absent (0), and escape. 
    #Maxwait function - setting the screen to wait 20 seconds for a response. I referenced the Pyschopy site for info on the maxwait attribute (https://www.psychopy.org/api/event.html)
    Prac_response = event.waitKeys(keyList = [Targ_present, Targ_absent, "escape"], maxWait=20)
    
   #If statment to handle the participant response and give feedback 

    if Prac_response is not None: #If the participant did respond 
        resp = Prac_response[0] #Take the first key that the pressed as the response 
        if resp == "escape": #If the participant responded with the escape key
            win.close() #Close the window 
            core.quit() #Quit the experiment 
        elif (pres == 1 and resp == "1") or (pres == 0 and resp == "0"): #Here I am setting a paramter to assign the correct response to incorrect and give feedback to the user
            #If target is present and the user pressed 1 = correct
            #If target is absent and the user presses 0 = correct
            feedback = "Correct!" #Creating text stimuli that will appear to user 
        else: #Anything else = Incorrect
            feedback = "Incorrect."
    else: #If no response at all 
        feedback = "No response."
        
#Creating the text stimuli that will appear the feedback to the participant 
    feedback_text = visual.TextStim(win, text=feedback, color="white", height=30)
    feedback_text.draw() #Drawing the stimuli
    win.flip() #Flipped to main window 
    core.wait(1) #Show on screen for 1 second 


#Creating a transition text for the particiapnt to know that the real experiment will now begin
Exp_Starttxt = (
    "Great!\n\n"
    "The practice trials are now over.\n\n"
    "The experiment will now begin.\n\n"
    "Press SPACE to continue or ESCAPE to exit")

#Creating the text stim that includes the crafted text I made and other parameters (positioning central, white, and height 30).
EXP_Start = visual.TextStim(
    win, 
    pos=(0, 0), 
    text = Exp_Starttxt, 
    color = "white", 
    height = 30)

EXP_Start.draw() #Drawing the stimulas
win.flip() #Flipping to the main window 

#Creating another key list response that will initialize the start of the main experiment 
#Space to continue, escape to exist 
Start = event.waitKeys(keyList = ["space","escape"]) 

##Starting the experimental for loop 

#This for loop is stating - For every value in the range of my total number trials (8) start/go through this loop. 
for trial_num in range (numb_Trials): 
    
    fixation.draw() #Drawing the fixation visual "+" to prepare it to be flipped onto the windows screen
    win.flip()  #Flippng the stimulas to the main window.
    core.wait(.5) #Allowing the fixation prompt to stay on the screen for .5 seconds. 
    
    present = Trial_Condition[trial_num] #Goes through all randomized 0-1 values from the trial_condition list and determines if the trial is a present or absent trial.
    
#If the target is present (value = 1), the Targ_pos (target position) will randoomly choose which position out of the 8 (positions) the stimulas gets. If it is not present than it will not assign a position, all stimulas will be L's (else none).
    Targ_pos = random.randrange(set_size) if present else None 
  
#This is a for loop inside of another for loop. This loops purpose is to assemble and draw all the letters on the main window
#It is saying that for every value in range of the current setSize (6,8,10), go through and place the amount of letter associated to that setSize, one at each position. 
#The first if statment is checking if the target is present and is it currently at the targets assigned position. If yes then it continues in the loop to place the T (target) at the position assigned upright. Then the T is drawn. 
#The else statment is if the first condition is not met. Thus, indicating that the position should show a distractor L. Following the same format, place L at a randomly assigned position and randomly pull from the list of given orientations (come from possibleOri list). Then the L is drawn.
    for i in range(set_size):
        if present and i == Targ_pos:
            Tstim.pos = positions[i]
            Tstim.ori = 0 
            Tstim.draw()
        else: 
            Lstim.pos = positions[i]
            Lstim.ori = random.choice(possibleOri) #Random.choice - randomly selects an element from given list. Referenced from W3schools (https://www.w3schools.com/python/ref_random_choice.asp)
            Lstim.draw()
        
    win.flip () #Flipping all of the above to the current working window

#Here I am creating another new clock object (called respClocl), which starts recording time starting from 0 seconds.
#I then reset my response clock so that it begins recording from 0 right after the stimulas is shown in the loop.
    respClock = core.Clock() #Start a new clock here
    respClock.reset() #Reset the clock to 0.00 seconds
    
#Here I am setting an if statment to allow the window to close if the participant chooses to press escape and leave the experiment
#If the participant selects escape using the keyboard, then it is set to close the window and quit the program. 
    if "escape" in keys:
        win.close()
        core.quit()

#Next I am starting to incorperate recording RT and accuracy of each trial response.

#I start by assigning a response variable to the participants key responses. 
#Again, keylist limit which keys are accepted and recorded, in this case target present (key 1), and target absent (key 0), are accepted or escape. 
#TimeStamped = respClock - this argument is apart of the event.waitkeys function, in which it lets you record the exact time in which the participant responds using the assigned keys.
#MaxWait function = setting the maximum trial length to be 40 seconds. If participant exeeds this length it will be count as "None" which is a missed trial.
#I referenced the Psychopy website for the timeStamped function (https://www.psychopy.org/api/event.html)
    response = event.waitKeys(keyList = [Targ_present, Targ_absent,"escape"], timeStamped = respClock, maxWait = 40.00)


#Here I am storing the current RT time from respClock into a new variable called RT
#The .getTime function allows for the coder to find out how long the participant took to respond to the given stimulas. 
#Referenced from W3Schools (https://www.w3schools.com/jsref/jsref_gettime.asp)
    RT = respClock.getTime() 
    
##Incorperating RT  

##Here I am formulating an if statment to check if a response was made, then recording that response and reaction time in a response list (inserting like a tuple of the key).
#I am also incorperating an if statment within this first statment to handle if the participant presses escape (exist experiment)
#I am then specifying that if no response was made the response is none or an empty list
    if response: #Checking if a key was pressed for this trial
        resp, RT = response[0] #Gets the key and RT from the response and stores it into response list together
        
        if resp == "escape": #If the participant presses escape, exit the experiment and close the program
            win.close()
            core.quit()
    else:
        resp, RT = None, None #If there was no key pressed (response list is empty for this trial). RT, Resp = None, means that there was no key response pressed or RT recorded.

##Calculate accuracy


#Here I have fomulated an if statment to check the accuracy of each trial response. 
#If the participant pressed a key in the keylist then this if statment would be activated. 
    if resp is not None: #This checks if the participant pressed a key. If they pressed nothing or the screen timed out then this would be none. If they did, then this if statment would proceed where it would check if the response was correct.
        if (present == 1 and resp == "1") or (present == 0 and resp == "0"): 
            #This is the accuracy check. It is specifying that the T (target) was present (present == 1), and the participant responded that they saw it (resp == 1)or there was no T (target) present (present == 0) and the participant responded that their was no T (resp == 0) 
            corr = 1 #If either of the above statments are true than we set it to correct response (1)
        else:
            corr = 0 #If the above statments are not true (participant responded yes to a target but their was not one), then it is set as an incorrect response (0).
    else:
        corr = 0 #If the participant did not give a response at all, then it is set to be incorrect (0).
    
    print(f"Trial {trial_num+1}: response={resp}, Correct={corr}",RT) #Printing the results of the trial. Printing the number of trials (starting from 1), what key was pressed  (0 or 1), if it was correct (correct or not), and the RT of that response.
#note - trial_num + 1 becasue starts at 0 


##Adding a overview of average RT and Accuracy

#Here I am recording participant data for each trial. 
#I am storing the RT and Accuracy data into two lists that I can later use to compute averages 
    if RT is not None: #If RT is not none (if the participant did respond; none = they did not respond) then store that trials RT in a list (All_RT list)
        All_RT.append(RT)
    else: #This line runs when there was no response recorded (missed trial)
        All_RT.append(None) #RT is now appended to my All_RT list as None
    All_Acc.append(corr) #Storing accuracy data (0 = incorrect, 1 = correct) to a list (All_Acc)
            

#This is list a comprehension, a new list created based from elemtents of an old list, I referenced W3Schools here (https://www.w3schools.com/python/python_lists_comprehension.asp). It is used to go through each RT in the All_RT list, if RT is not none (no response data) then it keeps it in the new list called Val_RT
#This ensures that the average RT is based strictly on trials that collected data 
Val_RT = [rt for rt in All_RT if rt is not None]

#Next I am calculating an average RT using the Val_RT (New list) and storing it into a new variable Mean_RT
#sum (Val_rt) is the sum of all valid RT trials being divided by len(Val_RT) which is how many RTs were in that new list
Mean_RT = sum(Val_RT) / len(Val_RT) if Val_RT else 0 #This is to avoid a potential error if the participant does not respond. It is saying if in the Val_RT list their is at least one RT response, calcuate the average, however if their is not then set the average to 0. 

#Next I am computing the mean accuracy and storing it into a new varible Mean_Acc
#sum(All_Acc) is the sum of all accuracy trials then divided by len(All_Acc) the length of total trials
Mean_Acc = sum(All_Acc) / len(All_Acc)
 
 
#Here I am printing out the results of the experimental statistics I just computed above. 
#The average RT and accuracy should print in the output section when the experiment is run. 
print(f"\n--- Participant Average RT and Accuracy Data ---") 
print(f"Average RT: {Mean_RT}") #Print from new Mean_RT variable (contains the average RT across trials)
print(f"Accuracy: {Mean_Acc * 100}") #Print from new Mean_Acc variable (contains the average accuracy across trials and muiltiple it by 100 to get percentage)


#Writing data to a Datafile - using the with function 
filename = f"Participant_{Participant_Number}_data.csv" #Creates a string that is associated with the participant number, which gets inserted into the file name. Example the data file would save as - Participant_Erin_data_.csv

with open(filename, 'w') as Datafile: #Opens a new file with the name created under filename. 'w' means write - creates a new file. The With function opens a file and ensures it closed once it leaves the block. Datafile is the varible within the with block, which identifies the file. 
    Datafile.write('Participant_Number,set_size,Mean_RT,Mean_Acc\n') #Writes the column sections in the CSV file 
    Datafile.write('%s, %i, %.3f, %.2f\n' % (Participant_Number, set_size, Mean_RT, Mean_Acc)) #This writes the next row of data using string formating (string, integer, float with 3 decimal, float with 2 decimals) 

#Using the with open (...) as datafile - will take care of closing the file after the code finishes writing without manually closing it. This ensures the file is always properly closed. 
#Here are the references I used that support this function and helped me formulate my code - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) (https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) (https://realpython.com/read-write-files-python/#working-with-file-objects)
#The with function appeared to be more effienct and easier to understand. 

#Here I have created an end text stim to appear on the window after the 8 trials are completed by the participant.
#end_txt is assigned to a visual text sim, which I then specify it to go on the main window with the given parameters (colour white, 30 height).
end_txt = visual.TextStim(
    win, 
    text="Thank you for participating in this experiment!\n\nPress any key to exit.", 
    color="white", 
    height=30
)

end_txt.draw() #I then draw the end_txt stimulas 
win.flip() #I then flipped the stimulas to appear on the main window 
event.waitKeys() #When a participant selects any key, this will allow them to exit the experiment and close the program. 

win.close() #Closing the window and quiting the program. 
core.quit()

