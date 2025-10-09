##Example
##Manually set up file and write after each trial before experiment begins 

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
    else:
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
    
    if (resp == 'left' and side[0] == 2) or (resp == 'right' and side[0] ==1):
        corr = 1
    else:
        corr = 0
    
    
respClock = core.Clock()

        
        
















