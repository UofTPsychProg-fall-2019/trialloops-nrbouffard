#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: nrbouffard
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
trialClock = core.Clock() # resets after each trial
expClock = core.Clock() # won't reset

# read in experiment info
trialInfo = pd.read_csv('objectConds.csv')

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))  
objectLeft = visual.ImageStim(win, image =trialInfo.loc[1,'object'] , pos= (-0.5,0.2))
#objectLeft = visual.ImageStim(win, image = 'objects/portapotty.jpg', pos= (-0.5,0.2))
faceRight = visual.ImageStim(win, image = trialInfo.loc[1,'face'],pos= (0.5,0.2))
#faceRight = visual.ImageStim(win, image = 'faces/1.jpg', pos= (0.5,0.2))
myScale = visual.RatingScale(win, low=1, high=7, marker='triangle',
    tickMarks=[1,2,3,4,5,6,7],markerStart=None,markerColor='black',pos = (0,-.6))
myText = visual.TextStim(win, text = 'vividness', pos = (0,-.25), color = 'black', height = .10) #note default color is white, which you can't see on a white screen!

# then draw all stimuli
objectLeft.draw() 
faceRight.draw()
myScale.draw()
myText.draw()

# then flip your window
win.flip()
# then record your responses
keys = event.waitKeys(keyList=['1','2','3','4','5','6','7'])
print(keys)

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(5)
win.close()
