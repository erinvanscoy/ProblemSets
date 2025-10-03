##Lecture 5 Notes Psychopy 
##Erin Vanscoy 2025/10/02 

##Example code 
from psychopy import visual, core #import the psychopy library (visual and core components)
win = visual.Window([400,400]) #Creating a window to draw too (win is an identifier, could be anything, just a name/variable). Called the visual.window method and had to specify the size of it [400,400]
message = visual.TextStim(win, text = 'hello') #Draw stimuli (using visual.textstim code, which will be displayed in win, and the text option is hello) - part of stimuli being displayed is the text hello
message.autoDraw = True #Setting one of the properities of the object to true, which is autodraw. Autodraw tells us that it is going to automatically draw every frame. 
win.flip() #Flip the stimulas present on the screen. Move from backbuffer to the display screen
core.wait(2.0) #Delay the next thing for 2 seconds. None of the following code occurs until the 2 seconds are over 
message.text = 'world' #Call the object created earlier (message) and modify the text of exisiting stimulas.
win.flip() #Then the new changes to the stimulas are flipped and display on display monitor
core.wait(2.0) #Delay of another 2 seconds before finished.

#win = visual.window([1024, 768], fullscr = false, units = 'pix']
## This is how you could edit the visual window. 

##Autdodraw true = means it will stay on the screen and draw it until we specificy it to go away. If it was autodraw false = then it would stop after being shown on one screen 
###Flip is important, stimulas will not appear until the buffer is flipped. If in a task you want things to appear fast, have to consider this in coding when you flip.



##Example

from psychopy import visual, event, core, data
win = visual.Window([1024,768], fullscr=False, units = 'pix')
#initialise some stimuli 
fixation = visual.Circle(win, size = 5, #because we set our units, we need to specify size (5) 
lineColor = 'white', fillColor = 'lightGrey')
probe = visual.GratingStim(win, size = 80, #'size' is 3xSD for gauss
pos = [300,0], 
tex = None, mask = 'gauss',
color = 'green')

cue = visual.ShapeStim(win,
vertices = [[-30,-20], [-30,20], [30,0]],
lineColor = 'red', fillColor = 'salmon')

info = {} #a dictionary
info['fixTime'] = 0.5 #seconds
info['cueTime'] = 0.2
info['probeTime'] = 0.2

#run one trial - Creating a single trial 
##run with main code alone 
fixation.autoDraw = True #This will stay on until you tell it to turn off, as oppose to draw 
win.flip()
core.wait(info['fixTime'])

cue.draw()
win.flip()
core.wait(info['coreTime'])

fixation.draw()
probe.draw()
win.flip()
core.wait(info['probeTime'])


##Run mulitiple trials, running a for loop 
#run with main code alone 
for trial in range(5):
    fixation.draw()
    win.flip()
    core.wait(info['fixTime'])
    
    cue.draw()
    win.flip()
    core.wait(info['coreTime'])
    
    fixation.draw()
    probe.draw()
    win.flip()
    core.wait(info['probeTime'])

##Task in class, using main code alone and adding on so that the trials are random and their muiltiple 

##Example

from psychopy import visual, event, core, data
import random 

win = visual.Window([1024,768], fullscr=False, units = 'pix')
#initialise some stimuli 

fixation = visual.Circle(win, size = 5, #because we set our units, we need to specify size (5) 
lineColor = 'white', fillColor = 'lightGrey') #predefined colours within the software

probe = visual.GratingStim(win, size = 80, #'size' is 3xSD for gauss
pos = [300,0], #This is the position of x and y cordinates, 
tex = None, mask = 'gauss', #Texture 
color = 'green')

cue = visual.ShapeStim(win,
vertices = [[-30,-20], [-30,20], [30,0]], ori=random.int,
lineColor = 'red', fillColor = 'salmon')

info = {} #a dictionary
info['fixTime'] = 0.5 #seconds
info['cueTime'] = 0.2
info['probeTime'] = 0.2

side = [1,2] ##two lists that have two values 
orient = [1,2]

#Create a series of trials that will randomly have valid and invalid trials 

for trial in range(5):
    random.shuffle(side)
    print("side: " + str(side[0])))
    random.shuffle(orient)
    print("orient: " + str(orient[0])))
    
    fixation.draw()
    win.flip()
    core.wait(info['fixTime'])
    
    if orient ==1:
        cue.ori = 0
    else: 
        cue.ori = 180
    
    cue.draw()
    win.flip()
    core.wait(info['cueTime'])
    
    if side[0] ==1:
        probe.pos = [30,0]
        else
        probe.pos = [-30,0]
        
    fixation.draw()
    probe.draw()
    win.flip()
    core.wait(info['probeTime'])

###Entire code but incorperating RT and Accuracy 

from psychopy import visual, event, core, data
import random 
respClock = core.Clock()
win = visual.Window([1024,768], fullscr=False, units = 'pix')
#initialise some stimuli 

fixation = visual.Circle(win, size = 5, #because we set our units, we need to specify size (5) 
lineColor = 'white', fillColor = 'lightGrey') #predefined colours within the software

probe = visual.GratingStim(win, size = 80, #'size' is 3xSD for gauss
pos = [300,0], #This is the position of x and y cordinates, 
tex = None, mask = 'gauss', #Texture 
color = 'green')

cue = visual.ShapeStim(win,
vertices = [[-30,-20], [-30,20], [30,0]],
lineColor = 'red', fillColor = 'salmon')

info = {} #a dictionary
info['fixTime'] = 0.5 #seconds
info['cueTime'] = 0.2
info['probeTime'] = 0.2

side = [1,2] ##two lists that have two values 
orient = [1,2]

#Create a series of trials that will randomly have valid and invalid trials 

for trial in range(5):
    random.shuffle(side)
    print("side: " + str(side[0]))
    random.shuffle(orient)
    print("orient: " + str(orient[0]))
    
    fixation.draw()
    win.flip()
    respClock
    
    if orient ==1:
        cue.ori = 0
    else: 
        cue.ori = 180
    
    cue.draw()
    win.flip()
    core.wait(info['cueTime'])
    
    if side[0] ==1:
        probe.pos = [30,0]
        else
        probe.pos = [-30,0]
        
    fixation.draw()
    probe.draw()
    win.flip()
    #core.wait(info['probeTime']) #no longer waiting 
    
    respClock.reset() #reset my clock 
    
    win.flip() #clear screen
    
    #Look for a keyboard response by assigning to a varible by keys 
    keys = event.waitKeys(keyList - ["left", "right", "escape"])
    resp = keys[0] #track the responses we got 
    rt = respClock.getTime() #calculate the reaction time of response 
    
    ##also calculate accuracy 
    
    if (resp == 'left' and side[0] == 2) or (resp == 'right' and side[0] ==1)
        corr = 1
    else:
        corr = 0
    
    
respClock = core.Clock()

##Writing Files in coding 
## open a file - fileID = open(filename, w)
##writing to file - fileID.write(format', vars)
#Format being sting, int etc 
##Manually set up file and write after each trial before experiment begins 
#At the end of the experiment, this is where you would want to close it (e.g., dataFile.close())

#Move a stimulas to a new location - change the pos 
#Present an image - imagestim (window[image address (path or what the image is), mask (mask stimulas that only displays specifics in the stimulas), units (how big you want it on display), pos (position you want it)
#Take a mouse input - class and then(incorperate event library) - (visable, position, win). When you create a mouse, you are creating a class.














