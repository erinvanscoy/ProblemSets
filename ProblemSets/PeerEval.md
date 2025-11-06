
## Erin Vanscoy Peer Evaluation 
## 2025/11/06

# Note for Dr. Emrich - The format of this document goes
1. A snippet of the peers code (in order)
2. My understanding of what they did (this helped me to evaluate the code) 
3. My feedback (on that snippet of code) 

# Code
# Experimental setup 
expName = 'VisualSearch' 
dlg = gui.Dlg()
dlg.addField('SubjectID:')
dlg.addField('Trials Per Cond:')
ok_data = dlg.show()
if not dlg.OK:
    core.quit()
    
sub_ID = ok_data[0]
trials = int(dlg.data[1])
fileName = sub_ID + "_" + expName
dataFile = open(fileName + '.csv', 'w')
dataFile.write('SetSize,TP, RT, Correct, Missed\n')

win = visual.Window([1920, 1080], fullscr=False, units='pix')
# Comments - What does this code mean 
-       expName = 'VisualSearch' 
- Here they are defining a string variable (expName)
-       dlg = gui.Dlg() 
- Here they are creating a dialog box using gui 
-       dlg.addFeild ('subjectID:') 
- Next they are adding their input field, this one being subject ID
-       dlg.addFeild ('trials per cond:') 
- Adding a field for the number of trials per condition
- Their dialog box with show two text boxes 
-       ok_data = dlg.show()
- Display dialog box on window, storing the data from fields into a new list
-       if not dlg.ok 
- If the user closed window or did not complete dialog window 
-       core.quit() 
- Quits the program/experiment if user cancelled dlg
-       sub_ID = ok_data[0] 
- This is indexing (pulling information) from the first value inputted in the dialog box (subject)
-       trials = int(dlg.data[1]) 
- This is indexing the second input from the dialog box (trials per cond)
-       fileName = sub_ID + "_" + expName 
- Makes a customizable filename to save data in 
-       dataFile = open(filename + '.csv', 'w') 
- This opens a csv file and writes it 
- The experimenter than created their window 

# Comments - Feedback for this code 
- One thing I liked about this code, especially when reflecting on how I incorporated the gui module, was that they did not hard code the input fields. This allows the experimenter/participant to fill in the inputs without any editing or changing to the code. This reduces errors and makes the code more transferable across subjects/conditions. 
- Thus, this keeps the code reusable and promotes efficiency. 
- I also liked how they incorporated a safeguard exit if the user cancels or closes the program. This ensures the program exits gracefully. 
- I really liked how the code was made in a way that adapts to the user input (#of trials, subject). The experimenter could run any number of trials based on inputting it and indexing it. 
- The coder directly tied the parameters to the data file which helps with tracking data and reduces experimental error

# Code
# Stimuli and Conditions
conditions = [5, 8, 12]
stim_size = 30
T = visual.ImageStim(win, 'Stimuli/T.png', size=stim_size)
L = visual.ImageStim(win, 'Stimuli/L.png', size=stim_size)

# Comments - What does this code mean 
-       conditions = [] 
- They are defining a list of set sizes 
-       stim_size = 30 
- Defining the size of each stim image 
-       T and L = visual.image(win, 'stimuli/l.png', size =stim_size) 
- Assigning T and L to the stim images, telling it where to be displayed, directing the path to find the images, specifying size

# Comments - Feedback for this code 
- One potential issue in future is hardcoding file paths to get to the images, if these files are missing or renamed the experiment will not work
- One benefit is defining the stim images only once here at the start, instead of constantly creating new object images

# Code
# Draw stimuli at random positions/orientations
def pos_and_ori(target, distract, samp_size):
    samplelist = list(range(-180, 180, 25))
    x = random.sample(samplelist, samp_size)
    y = random.sample(samplelist, samp_size)
    for n in range(0, samp_size - 1):
        orientations = [0, 90, 180, 270]
        orin = random.choice(orientations)
        distract.ori = orin
        distract.pos = (x[n], y[n])
        distract.draw()
    for n in range(samp_size - 1, samp_size):
        target.pos = (x[n], y[n])
        target.draw()
    return distract, target

# Comments - What does this code mean 
-       def pos_and_ori(target, distract, samp_size):
- Defining a function that takes three arguments (target, distract, sample size)
-       samplelist = list(range)
- Creates a list of numbers to be potential x or y coordinates 
- x y = random.sample(samplelist, samp_size)- Select random x and y coordinates depending on samp size 
-       For n in range(0, samp_size -1) 
- A for loop that goes through all but the last position
-       orientations = [] 
- List of given orientations
-       orin = random.choice (orientation) 
- Select a random orientation from list
-       distract.ori = orin
- Puts distractor in its orientation 
-       distract.pos = (x[n], y[n])
- Puts it in its screen position 
-       distract.draw() 
- Draws it on main window 
-       for n in range(samp_size -1, samp_size) 
- Another for loop, this is run only once for the last position in the list 
-       target.pos = (x[n], y[n]) 
- Puts target at the last coordinate
-       target.draw() 
- Draws the target on main window 
-       return distract, target 
- Returning the two stimulus objects 

# Comments - Feedback for this code
- I really liked how the coder put this into a function. This seemed like a smart design choice, as it makes the code reusable, and transferable. The experimenter is now able to call the function repeatedly for different stimuli and trials
- I liked how the coder used randomization to randomize the positions of the items and their orientations. This ensures each trial will appear slightly different

# Code 
# Determine if target is present on a given trial
def targ_pres(trial_list, total_trials, distract, target, condition_index):
    pres_or_not = random.choice(trial_list)
    trial_list.remove(pres_or_not)
    if pres_or_not <= np.median(total_trials):
        targ_there = 0
        stimuli = pos_and_ori(distract, distract, condition)
    else:
        targ_there = 1
        stimuli = pos_and_ori(target, distract, condition)
    return targ_there, stimuli

# Comments - What is this code doing 
-       def targ_pres(trial_list, total_trials, distract, target, condition_index):
- A function set with 5 parameters (list of trial numbers, total number of trials, distracter stim, target stim, which condition/setsize)
-       pres_or_not = random.choice(trial_list)  
- Randomily choose only value from the list
-       trial_list.remove(pres_or_not) 
- Remove that trial from list (so not chosen again)
-     if pres_or_not <= np.median(total_trials):
        targ_there = 0
        stimuli = pos_and_ori(distract, distract, condition)
        else:
        targ_there = 1
        stimuli = pos_and_ori(target, distract, condition)
- Used to split the trials 50/50 targ present and absent       
- If the target is not present, calls earlier function but puts distracter in both arguments
- Else the target was present, calling function and inputting target and distracter
-       return targ_there, stimuli 
- Function returns two things, whether the target was there and the stimulus object

# Comments - Feedback on this code
- One error in the code was in the IF statement, the coder used condition as the variable and I believe it should be condition_index 
- I really liked how the target being present or absent was wrapped into another function, I think this made the code very efficient and concise
- One potential error is using the median split to determine if the target was present or absent. This assumes the trial list will be divided evenly, which may not always be true. This method can not guarantee that exactly 50% of the trials will have a target present
- I did like how the coder called on their previous function in this function, I think it was very efficient in terms of determining if the target was present/or absent and placing the stimuli in their coordinates/orientations

# Code 
# Get response and RT
def KeyGet(trial_duration=2.0, rt=None, resp=None):
    startTime = core.getTime()
    while core.getTime() - startTime < trial_duration and resp is None:
        keys = event.getKeys(keyList=['a', 'd', 'escape'])
        if keys:
            key = keys[0]
            rt = core.getTime() - startTime
            if key == 'a':
                resp = 'a'
                break
            elif key == 'd':
                resp = 'd'
                break
            elif key == 'escape':
                core.quit()
        core.wait(0.01)
    if resp is None:
        resp = 'no_response'
        rt = 999
    return resp, rt

# Comments - What is this code doing 
-       def KeyGet(trial_duration=2.0, rt=None, resp=None): 
- Defining a function that uses the KeyGet module. KeyGet function will wait for the participant response (key press). Sets a maximum 2 second trial duration, then sets RT and response to start as none 
-       startTime = core.getTime() 
- Records the current time from start of trial
-       while core.getTime() - startTime < trial_duration and resp is None:
        keys = event.getKeys(keyList=['a', 'd', 'escape'])
- Loops until either the time limit runs or (2sec) or the participant responds. Sets the allowed keys to a variable (keys) using getkeys function and keylist
-          if keys:
            key = keys[0]
            rt = core.getTime() - startTime 
- If statement that runs if a key was pressed. Takes the first indexed key in the list and calculates the RT (time since the trial started)
-             if key == 'a':
                resp = 'a'
                break
            elif key == 'd':
                resp = 'd'
                break
            elif key == 'escape':
                core.quit()
        core.wait(0.01)
- This if statement then depending on which key is pressed assigns it to response. If escape is pressed the experiment ends 
-         core.wait(0.01)
- Wait 10ms 
-     if resp is None:
        resp = 'no_response'
        rt = 999
        return resp, rt
- If statement if no response was made. If no response, it gets set to no_response, and rT is set to 999 


# Comments - Feedback for code 
- Putting this into a function is a good way to reuse this piece of code for multiple experiments, however, the coder could have inputted the keylist as an argument so that they could customize the key list when calling the function. This would make this piece of code more reusable across different experiments (changing keys)
- The event.getKeys() is a good way to get key presses, however the coder could have implemented the timeStamped = respClock when defining their keys variable. Without timeStamped, the user only knows which key was pressed but when it's included they get timestamped tuples (key, RT). The coder could then remove the line of code where they manually calculated RT

# Evaluate response accuracy and feedback
def Response(resp, rt, targ_there):
    if resp == 'd' and targ_there == 1:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
    elif resp == 'a' and targ_there == 1:
        corr = 0
        feedback = 'Incorrect!'
        response_time = round(rt, 2)
    elif resp == 'a' and targ_there == 0:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
    elif resp == 'd' and targ_there == 0:
        corr = 0
        feedback = 'Incorrect'
        response_time = round(rt, 2)
    elif resp == 'no_response':
        corr = 0
        feedback = 'No Response'
        response_time = 'NA'
    return corr, feedback, response_time

# Comment - What is this code doing 
-       def Response(resp, rt, targ_there):
- A function that takes three inputs (resp a,d, no resp), (rt, target_there (1,0)
-     if resp == 'd' and targ_there == 1:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
- Each of these if and elif statements are checking a potential scenario. 
- This if statement is saying if target is present then its correct 
- Stores the RT at 2 decimal places in response_time 
-     elif resp == 'a' and targ_there == 1:
        corr = 0
        feedback = 'Incorrect!'
        response_time = round(rt, 2)
        elif resp == 'a' and targ_there == 0:
- If the target was present but the participant pressed an incorrect key, it is an incorrect trial. Store RT in response_time at 2 decimal places
-     elif resp == 'a' and targ_there == 0:
        corr = 1
        feedback = 'Correct!'
        response_time = round(rt, 2)
- If the target was absent and the participant pressed the correct key then it's correct. Store RT in response_time at 2 decimal places
-     elif resp == 'd' and targ_there == 0:
        corr = 0
        feedback = 'Incorrect'
        response_time = round(rt, 2)
- If the target was absent but the participant pressed an incorrect key, the trial is incorrect. Store RT in response_time with 2 decimal places
-     elif resp == 'no_response':
        corr = 0
        feedback = 'No Response'
        response_time = 'NA'
- If no response, the trial is incorrect but feedback is set at no response and RT is implemented in response_time as N/A
-       return corr, feedback, response_time
- Returns outputs based on correct response, feedback, and response time. 

# Comments - Feedback for code 
- This piece of code is very detailed and easy to understand, however, I think it could have been condensed into a more efficient code to avoid repetition 
- Here is an example of an alternative way the coder could eliminate repetitive code and generate response accuracy/feedback (note. the indenting in this example is incorrect, it is just to show an alternative way one could compute this code)

        def Response(resp, rt, targ_there):
            if resp == 'no_response':
            return 0, 'No Response', 'NA'
            correct_key = 'd' if targ_there == 1 else 'a'
            corr = int(resp == correct_key)
            feedback = 'Correct!' if corr else 'Incorrect!'
            response_time = round(rt, 2)
            return corr, feedback, response_time

- In this example, the function is still taking three arguments (resp, rt and targ_there). It is saying if the response is equal to no response, return 0 (incorrect), no response, and NA 
- Then the correct_key is defined - If the target was present, then the correct key is (d), else the target is absent thus the correct key is (a)
- Then it checks if the key response matches the correct key (true = 1, false = 0) 
- Then feedback gets generated - if correct (1) else incorrect(0) 
- Then rounds the RT at the end to 2 decimal places 
- Then returns the correct (0,1), feedback message, and RT (2 decimal places)
- This method may offer a more efficient way to check the accuracy of the response and return feedback, RT, and accuracy. 

# Code 
# Instructions
welcome = ''''
Welcome to the Visual Search Task

You will see an assortment of shapes in different positions and orientations.
Most will be 'L' shapes, but some may contain a 'T' shape.

If the T is present, press 'd'.
If the T is absent, press 'a'.

Respond quickly!
Press SPACE to begin 5 practice trials.
'''

instructions = visual.TextStim(win, color='white', text=welcome, units='norm', height=0.05)
instructions.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])
core.wait(0.25)

# No general comments/feedback for this section 
- Other than the instructions were well versed and concise

# Code 
# Practice trials
practice_trials = range(1, 6)
for condition in conditions:
    appear = list(practice_trials)
    for prac_trials in practice_trials:
        targ_there, stimuli = targ_pres(appear, practice_trials, L, T, condition)
        resp, rt = KeyGet()
        corr, feedback, response_time = Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)

# Comments - What is this code doing 
-       practice_trials = range(1, 6)
- Creates a list of numbers between 1-5
-       for condition in conditions:
- For loop that goes through different conditions 
-       appear = list(practice_trials)
- Converts the practice trials into a list under appear variable 
-     for prac_trials in practice_trials:
        targ_there, stimuli = targ_pres(appear, practice_trials, L, T, condition)
        resp, rt = KeyGet()
        corr, feedback, response_time =
- Loops through each practice trial 1-5
- Calls the targ_pres function (which will decide if the target is present)
- Calls keyGet function to measure RT 
-       corr, feedback, response_time =  Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)
- Calls the response function to check if the response was correct and generate feedback/ round RT 
- Creates two text objects to display feedback message and RT

# Comments - Feedback on code
- I liked how this code gave the participant immediate feedback (correct/incorrect) and RT after each trial 
- Defining separate functions to do each main component of the experiment is very concise and will make debugging easier because each function focused on a single aspect of the experiment. The coder can then go back into their function (if need be) to add or adjust anything relevant to its task. 

# Code
# Main experiment instructions
welcome = ''''
Practice complete! Now for the real trials.

Press SPACE to begin.
'''
instructions = visual.TextStim(win, color='white', text=welcome, units='pix', height=10)
instructions.draw()
win.flip()
keys = event.waitKeys(keyList=['space'])
core.wait(0.25)
- 
# No comments for this piece of code

# Code
# Trial setup
total_trials = range(1, trials + 1)
rt_list, corr_list, miss_rt_list = [], [], []
random.shuffle(conditions)

# Comments - What is this code doing 
-       total_trials = range(1, trials + 1)
- Creates an iteration of trial numbers starting from 1 to the total number of trials. 
-       rt_list, corr_list, miss_rt_list =  [], [], [] random.shuffle(conditions)
- Creates empty lists to store the data in (RT, correct, missed RTs)
- Then random shuffle the conditions 

# Comments - Feedback on code 
- Creating a variable that represents the sequence of trials from 1 to the number of trials is a good way to avoid hard coding, as this will adapt to whatever the number of trials equals
- Creating these empty lists to store data outside of the loop ensures ALL trial data will be stored accordingly later in your code

# Code
# Main experiment loop
for condition in conditions:
    appear = list(total_trials)
    for trial in total_trials:
        targ_there, stimuli = targ_pres(appear, total_trials, L, T, condition)
        resp, rt = KeyGet()
        corr, feedback, response_time = Response(resp, rt, targ_there)
        cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)
        if rt != 999:
            rt_list.append(rt)
            miss_rt = 0
            corr_list.append(corr)
        else:
            miss_rt_list.append(1)
            miss_rt = 1
            corr_list.append(0)

dataFile.write('%i, %i, %.3f, %i, %i\n' % (condition, targ_there, rt, corr, miss_rt))

dataFile.close()

# Comment - What is this code doing 
-       for condition in conditions:
        appear = list(total_trials)
- This for loop will loop through experimental condition, appear is the list of trial numbers for that specific condition
-       for trial in total_trials:
        targ_there, stimuli = targ_pres(appear, total_trials, L, T, condition)
        resp, rt = KeyGet()
        corr, feedback, response_time = Response(resp, rt, targ_there)
- Loops through each trial, calls the function targ_present to determine if target is present or absent and which stim will be shown
- Waits for a key response from participant, collects RT 
- Checks if the participant responded correctly by calling response function 
-       cor_feedback = visual.TextStim(win, text=feedback, pos=(0, 30), height=40)
        back_rt = visual.TextStim(win, text=response_time, pos=(0, -30), height=40)
        cor_feedback.draw()
        back_rt.draw()
        win.flip()
        core.wait(0.5)
- Creates text stim for feedback and RT 
- Draws on screen 
-         if rt != 999:
            rt_list.append(rt)
            miss_rt = 0
            corr_list.append(corr)
        else:
            miss_rt_list.append(1)
            miss_rt = 1
            corr_list.append(0)
- If participant responded, adds RT to rt_list, Inputs miss_rt as 0 (no missed trials, and adds correctness to corr_list 
- If participant did not respond, adds a 1 o miss RT list to suggest a missed trial and sets correct to 0
-       dataFile.write('%i, %i, %.3f, %i, %i\n' % (condition, targ_there, rt, corr, miss_rt)) dataFile.close()
- Writes a line of code for each trial into a file (condition, targ present, RT, if correct, and missed RT response)
- Closes the file safely 

# Comment - Feedback for code
- I liked how the coder considered their data logging, as it writes to the file after each trial. 
- Having 999 as an indicator for a missed trial can be a little bit confusing for the reviewer, perhaps defining a constant to 999 would yield more clarity in this part of the code
- Another suggestion would be to create the correct feedback / RT feedback textStim objects outside of the loop and adjust the .text attribute within the loop on each trial. This is more efficient inside the loop 

# Code 
# Final feedback
average_rt = round(np.mean(rt_list), 2)
average_corr = round(np.mean(corr_list), 2)
total_miss = sum(miss_rt_list)

avg_rt_text = f'average rt: {average_rt}'
avg_corr_text = f'average correct: {average_corr}'
miss_text = f'no response on {total_miss} trials'
leave_text = 'press SPACE to exit'

cor_avg_back = visual.TextStim(win, text=avg_corr_text, pos=(0, 50), height=20)
rt_avg_back = visual.TextStim(win, text=avg_rt_text, pos=(0, -10), height=20)
miss_tot_back = visual.TextStim(win, text=miss_text, pos=(0, -35), height=20)
exit_text = visual.TextStim(win, text=leave_text, pos=(0, -100), height=20)

cor_avg_back.draw()
rt_avg_back.draw()
miss_tot_back.draw()
exit_text.draw()

win.flip()
keys = event.waitKeys(keyList=['space'])
win.close()
core.quit()

# Comment - What is this code doing 
- Computing the summary stats (average RT, average correct, and total misses)
- Then creating text strings to display these stats 
- Creating textstim objects to display these stats on the main window 
- Then drawing and displaying them on main window 

# Comment - Feedback on code 
- The average accuracy may be more intuitive for participants as a percentage 

# Overall feedback 
- The structure of this code was extremely easy to follow. Starting by creating functions and then implementing them in the for loops provided a concise and transferable code
- Having separate functions for the main components of the experiment also allows the coder to manually adjust or implement anything into that function without disrupting other parts of their code
- The data logging was concise and provided a trial to trial summary of results, which is extremely beneficial when analyzing data later 
- Great instructions, feedback, and summary stats for the participant to follow along 
- Using intuitive variable names can help with the flow and comprehension of the code 
- The repeated Textstim creation inside the loops may be somewhat inefficient, perhaps creating these outside the loops and updating them with the .text function would be better 
- There were some minor suggestions regarding improving efficiency within the functions
- Overall, this code was well done and had a lot of concise and efficient aspects
