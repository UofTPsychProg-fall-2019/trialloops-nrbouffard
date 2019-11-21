#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# create a gui object
subgui = gui.Dlg()
subgui.addField("Subject ID:")
subgui.addField("Session Number:")

# show the gui
subgui.show()

# put the inputted data in easy to use variables
subjID = subgui.data[0]
sessNum = subgui.data[1]

#%% prepare output

ouputFileName = 'data' + os.sep + 'sub' + subjID + '_sess' + sessNum + '.csv'
if os.path.isfile(ouputFileName) :
    sys.exit("data for this session already exists")

outVars = ['subj', 'trial', 'face', 'object', 'sceneFace', 'color', 'rating', 'rt', 'stimOn']    
out = pd.DataFrame(columns=outVars)

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
trialClock = core.Clock() # resets after each trial
expClock = core.Clock() # won't reset
stimClock = core.Clock()

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things

# read in experiment info
trialInfo = pd.read_csv('objectConds.csv')

myScale = visual.RatingScale(win, low=1, high=7, marker='triangle',
    tickMarks=[1,2,3,4,5,6,7],markerStart=None,markerColor='black',pos = (0,-.6))

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']

# randomize trials
trialInfo = trialInfo.sample(frac=1)
trialInfo = trialInfo.reset_index()

# set stimulus times in seconds
isiDur = 1
stimDur = 3

# set number of trials
nTrials = len(trialInfo)

# make your loop
for t in np.arange(0,nTrials) :
    
    # include your trial code in your loop but replace anything that should 
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!
    
    trialClock.reset()
    
    objectLeft = visual.ImageStim(win, image =trialInfo.loc[t,'object'] , pos= (-0.5,0.2))
    faceRight = visual.ImageStim(win, image = trialInfo.loc[t,'face'],pos= (0.5,0.2))
    myText = visual.TextStim(win, text = 'vividness', pos = (0,-.25), color = 'black', height = .10) 

    # then draw all stimuli
    objectLeft.draw() 
    faceRight.draw()
    myScale.draw()
    myText.draw()

    # record trial prarameters
    out.loc[t,'object'] = trialInfo.loc[t,'object']
    out.loc[t,'color'] = trialInfo.loc[t,'color']
    out.loc[t,'face'] = trialInfo.loc[t,'face']
    out.loc[t,'sceneFace'] = trialInfo.loc[t,'sceneFace']
    out.loc[t,'trial'] = t + 1
    
    # do nothing while isi is still occuring
    while trialClock.getTime() < isiDur:
        core.wait(.001)

    # then flip your window
    win.flip()
    stimClock.reset()
    # record when stimulus was prsented
    out.loc[t, 'stimOn'] = expClock.getTime()
    
    myScale.reset()  #reset rating scale right before drawing for RT
    while myScale.noResponse and stimClock.getTime()<stimDur:
            faceRight.draw()
            objectLeft.draw()
            myScale.draw()
            myText.draw()
            win.flip()
    
    # save responses       
    if myScale.noResponse == False: #if response was made
        out.loc[t, 'rating'] = myScale.getRating()
        out.loc[t, 'rt'] = myScale.getRT() 

# finish experiment
win.flip() 
core.wait(1)
 
goodby = visual.TextStim(win, text="""Thank you for participating
                         
Please get the experimenter""", height=.05, color = 'black')  
goodby.draw()
win.flip()

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

# manage output    
out['subj'] = subjID
out.to_csv(ouputFileName, index = False)


core.wait(4)
win.close()
core.quit()
