##PSYC 5P02 lecture 6 notes - Review 


from psychopy import visual, core, event ##importing libraries from psychopy 
win = visual.Window([400, 400]) #using visual library, and defining monitor setting and size of the visual stimuli 
message = visual.TextStim(win, text='hello') #Puts text on the window that you specifiy (visual.textStim - whatever is in that visual package that you want), inserting it on the win window you just created and the message you want displayed
message.autoDraw = True ##This is drawing the message we just created (message), so it appears on the screen
win.flip() ##Getting the code on the screen - moving it from backbuffer on the display 
core.wait(2.0)
message.text = 'world' ##Modifying the text in the file, pointng to message (place holder for that code) and .text to change the message. 
win.flip()  ##Getting the new modifications of the code on the screen (experimental showing screen) 
core.wait(2.0)


##Modifying text
##If you modify text or display later in the code, it will appear when you run that new modifcation code. If you want the modification at the first appearance of that code, you need to edit that first code. 

##Variable - something you can changea and create of your own
##Objectives - come from classess, they have certain properities or things you must follow (e.g., - win = visual.window([400,400]))

##auto draw - draw comand - will draw something on a frame 
##

from psychopy import visual, core ##importing libraries from psychopy 
win = visual.Window([400, 400]) #using visual library, and defining monitor setting and size of the visual stimuli 
message = visual.TextStim(win, text='hello') #Puts text on the window that you specifiy (visual.textStim - whatever is in that visual package that you want), inserting it on the win window you just created and the message you want displayed
message2 = visual.textStim(win, text = 'world')
message.autoDraw = True ##This is drawing the message we just created (message), so it appears on the screen
message2.autoDraw = True ##Creating a new message to appear 
win.flip() ##Getting the code on the screen - moving it from backbuffer on the display - but will display both messages at the same time
core.wait(2.0)

##Better solution 
from psychopy import visual, core ##importing libraries from psychopy 
win = visual.Window([400, 400]) #using visual library, and defining monitor setting and size of the visual stimuli 
message = visual.TextStim(win, text='hello') #Puts text on the window that you specifiy (visual.textStim - whatever is in that visual package that you want), inserting it on the win window you just created and the message you want displayed
message2 = visual.textStim(win, text = 'world')
message.autoDraw = True
message.autoDraw = False ##Turn off the first stimuli and then can turn on the next one
message2.autoDraw = True ##Creating a new message to appear 
win.flip() ##Getting the code on the screen - moving it from backbuffer on the display - but will display both messages at the same time
core.wait(2.0)

##
timer = core.clock() #timer is the clock within the while loop 
x,y = 0.0
starttime = timer.getTime() 

while timer.getTime - startime < 2.0: #convention you may want to use instead of core.wait, current time - when the time first started (will loop through current code) 
    x += 0.01 
    y += 0.01

    message.pos= (x,y)
    message.draw() ##Before every flip of the screen, specifiying to draw 
    win.flip()

##if you want a convention that lasts a certatin amount of time 

##How do you make the mouse follow the text (user input) 
##Make a mouse, find out where that mouse is, and update the position of the text to follow the mouse 

timer = core.clock() #timer is the clock within the while loop 
mouse = event.mouse (visible=True)
x,y = 0.0 
starttime = timer.getTime() 

while timer.getTime - startime < 20.0: #convention you may want to use instead of core.wait, current time - when the time first started (will loop through current code) 
    # x = mouse.getPost()[0] #mouse is an object - getPos, is calling the method and get position, () - calling the method and [] and returning it 
    # y = mouse.getPos()[1]
    
    pos = mouse.getPos() #Assigning the mouse.getposition to a object 
    message.pos= (pos[0], pos[1]) 
    message.draw() ##Before every flip of the screen, specifiying to draw 
    win.flip()
    
    
##keybord responses - different options explain this in assignments etc what one you use 
    
##Mask code - masking a face in an image to only capture the faces 

##Top of experiment open a file - dataFile.write - follow this in the slideshow to save outputs of the experiment 






