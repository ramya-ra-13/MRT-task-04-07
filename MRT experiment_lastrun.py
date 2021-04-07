#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Wed Apr  7 16:44:05 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'MRT experiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'email': '', 'session': '', 'date': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ramyaramakrishnan/Documents/gan-college/RA/MRT folder/MRT experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Hello"
HelloClock = core.Clock()
title = visual.TextStim(win=win, name='title',
    text='Welcome to the Mental Rotation Task.',
    font='Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
respintro = keyboard.Keyboard()
spac = visual.TextStim(win=win, name='spac',
    text='Press the spacebar to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
win.mouseVisible = False

# Initialize components for Routine "Instrux"
InstruxClock = core.Clock()
Intro = visual.TextStim(win=win, name='Intro',
    text='In this experiment, you will be asked to evaluate drawings of two objects. Sometimes they will be the same figure but rotated. Sometimes they will be mirror images of each other. Your job is to press “x” when the figures are the SAME and “m” when the figures are DIFFERENT.\n\nPlease do this as quickly and as accurately as you can.',
    font='Times New Roman',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
spac2 = visual.TextStim(win=win, name='spac2',
    text='Please press spacebar to see an example.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "VisualInstrux1"
VisualInstrux1Clock = core.Clock()
headerx = visual.TextStim(win=win, name='headerx',
    text='These two objects are the same but are rotated. \nIn this example, you will press “x”.',
    font='Times New Roman',
    pos=(0, 0.25), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Image1 = visual.ImageStim(
    win=win,
    name='Image1', 
    image='recodingtask_1/en15.jpg', mask=None,
    ori=0, pos=(-0.3, -0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
Image2 = visual.ImageStim(
    win=win,
    name='Image2', 
    image='recodingtask_1/en17.jpg', mask=None,
    ori=0, pos=(0.3, -0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
key_resp_3 = keyboard.Keyboard()
spac3 = visual.TextStim(win=win, name='spac3',
    text='Press “x” to continue.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "VisualInstrux2"
VisualInstrux2Clock = core.Clock()
headerm = visual.TextStim(win=win, name='headerm',
    text='These two objects are mirror images of each other. They can never be rotated to appear exactly alike. \nIn this example, you will press “m”.',
    font='Times New Roman',
    pos=(0, 0.25), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Image3 = visual.ImageStim(
    win=win,
    name='Image3', 
    image='recodingtask_1/ep17.jpg', mask=None,
    ori=0, pos=(-0.3, -0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
Image4 = visual.ImageStim(
    win=win,
    name='Image4', 
    image='recodingtask_1/en17.jpg', mask=None,
    ori=0, pos=(0.3, -0.1), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
key_resp_4 = keyboard.Keyboard()
spac4 = visual.TextStim(win=win, name='spac4',
    text='Press “m” to continue',
    font='Times New Roman',
    pos=(0, -0.4), height=0.040, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
practice = visual.TextStim(win=win, name='practice',
    text='Let’s do some practice. \n\nPress “x” if the two objects are the same. \nPress “m” if the two objects are mirror images (ie. the images cannot be superimposed on each other).\n\n',
    font='Times New Roman',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Practiceresponse = keyboard.Keyboard()
spac5 = visual.TextStim(win=win, name='spac5',
    text='Press spacebar to start.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixa = visual.TextStim(win=win, name='fixa',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StimDisplay"
StimDisplayClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(-0.35, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=(0.35, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg = ""
show = visual.TextStim(win=win, name='show',
    text='default text',
    font='Times New Roman',
    pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0, 
    color='Beige', colorSpace='rgb', opacity=2, 
    languageStyle='LTR',
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Times New Roman',
    pos=(0, -0.05), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
space = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Press the spacebar to continue\n',
    font='Times New Roman',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
answered = visual.TextStim(win=win, name='answered',
    text='default text',
    font='Times New Roman',
    pos=(-0.05, 0.07), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
answer = visual.TextStim(win=win, name='answer',
    text='default text',
    font='Times New Roman',
    pos=(0.15, 0.07), height=0.05, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "Start"
StartClock = core.Clock()
text3 = visual.TextStim(win=win, name='text3',
    text='You are now ready to start the experiment.\n\nRemember to do this task as quickly and accurately as you can. \n\nDo you have any questions? If so, please ask them to your experimenter promptly. If not, let the experimenter know that you are ready.\n',
    font='Times New Roman',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press the spacebar when you are ready to start the experiment.',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixa = visual.TextStim(win=win, name='fixa',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "StimDisplay1"
StimDisplay1Clock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(-0.35, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0.35, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
Final = visual.TextStim(win=win, name='Final',
    text='You have reached the end of the MRT task. \n\nThank you for your participation!',
    font='Times New Roman',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Press the spacebar to exit the current MRT task. ',
    font='Times New Roman',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Hello"-------
continueRoutine = True
# update component parameters for each repeat
respintro.keys = []
respintro.rt = []
_respintro_allKeys = []
# keep track of which components have finished
HelloComponents = [title, respintro, spac]
for thisComponent in HelloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HelloClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Hello"-------
while continueRoutine:
    # get current time
    t = HelloClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HelloClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *title* updates
    if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title.frameNStart = frameN  # exact frame index
        title.tStart = t  # local t and not account for scr refresh
        title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
        title.setAutoDraw(True)
    
    # *respintro* updates
    waitOnFlip = False
    if respintro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respintro.frameNStart = frameN  # exact frame index
        respintro.tStart = t  # local t and not account for scr refresh
        respintro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respintro, 'tStartRefresh')  # time at next scr refresh
        respintro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respintro.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respintro.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respintro.status == STARTED and not waitOnFlip:
        theseKeys = respintro.getKeys(keyList=['space'], waitRelease=False)
        _respintro_allKeys.extend(theseKeys)
        if len(_respintro_allKeys):
            respintro.keys = _respintro_allKeys[-1].name  # just the last key pressed
            respintro.rt = _respintro_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spac* updates
    if spac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spac.frameNStart = frameN  # exact frame index
        spac.tStart = t  # local t and not account for scr refresh
        spac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spac, 'tStartRefresh')  # time at next scr refresh
        spac.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HelloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Hello"-------
for thisComponent in HelloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('title.started', title.tStartRefresh)
thisExp.addData('title.stopped', title.tStopRefresh)
thisExp.addData('spac.started', spac.tStartRefresh)
thisExp.addData('spac.stopped', spac.tStopRefresh)
# the Routine "Hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instrux"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstruxComponents = [Intro, key_resp_2, spac2]
for thisComponent in InstruxComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstruxClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instrux"-------
while continueRoutine:
    # get current time
    t = InstruxClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstruxClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro* updates
    if Intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro.frameNStart = frameN  # exact frame index
        Intro.tStart = t  # local t and not account for scr refresh
        Intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro, 'tStartRefresh')  # time at next scr refresh
        Intro.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spac2* updates
    if spac2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spac2.frameNStart = frameN  # exact frame index
        spac2.tStart = t  # local t and not account for scr refresh
        spac2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spac2, 'tStartRefresh')  # time at next scr refresh
        spac2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstruxComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instrux"-------
for thisComponent in InstruxComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro.started', Intro.tStartRefresh)
thisExp.addData('Intro.stopped', Intro.tStopRefresh)
thisExp.addData('spac2.started', spac2.tStartRefresh)
thisExp.addData('spac2.stopped', spac2.tStopRefresh)
# the Routine "Instrux" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VisualInstrux1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
VisualInstrux1Components = [headerx, Image1, Image2, key_resp_3, spac3]
for thisComponent in VisualInstrux1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VisualInstrux1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VisualInstrux1"-------
while continueRoutine:
    # get current time
    t = VisualInstrux1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VisualInstrux1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *headerx* updates
    if headerx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerx.frameNStart = frameN  # exact frame index
        headerx.tStart = t  # local t and not account for scr refresh
        headerx.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerx, 'tStartRefresh')  # time at next scr refresh
        headerx.setAutoDraw(True)
    
    # *Image1* updates
    if Image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Image1.frameNStart = frameN  # exact frame index
        Image1.tStart = t  # local t and not account for scr refresh
        Image1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image1, 'tStartRefresh')  # time at next scr refresh
        Image1.setAutoDraw(True)
    
    # *Image2* updates
    if Image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Image2.frameNStart = frameN  # exact frame index
        Image2.tStart = t  # local t and not account for scr refresh
        Image2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image2, 'tStartRefresh')  # time at next scr refresh
        Image2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['x'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spac3* updates
    if spac3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spac3.frameNStart = frameN  # exact frame index
        spac3.tStart = t  # local t and not account for scr refresh
        spac3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spac3, 'tStartRefresh')  # time at next scr refresh
        spac3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VisualInstrux1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VisualInstrux1"-------
for thisComponent in VisualInstrux1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('headerx.started', headerx.tStartRefresh)
thisExp.addData('headerx.stopped', headerx.tStopRefresh)
thisExp.addData('Image1.started', Image1.tStartRefresh)
thisExp.addData('Image1.stopped', Image1.tStopRefresh)
thisExp.addData('Image2.started', Image2.tStartRefresh)
thisExp.addData('Image2.stopped', Image2.tStopRefresh)
thisExp.addData('spac3.started', spac3.tStartRefresh)
thisExp.addData('spac3.stopped', spac3.tStopRefresh)
# the Routine "VisualInstrux1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VisualInstrux2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
VisualInstrux2Components = [headerm, Image3, Image4, key_resp_4, spac4]
for thisComponent in VisualInstrux2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VisualInstrux2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VisualInstrux2"-------
while continueRoutine:
    # get current time
    t = VisualInstrux2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VisualInstrux2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *headerm* updates
    if headerm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        headerm.frameNStart = frameN  # exact frame index
        headerm.tStart = t  # local t and not account for scr refresh
        headerm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(headerm, 'tStartRefresh')  # time at next scr refresh
        headerm.setAutoDraw(True)
    
    # *Image3* updates
    if Image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Image3.frameNStart = frameN  # exact frame index
        Image3.tStart = t  # local t and not account for scr refresh
        Image3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image3, 'tStartRefresh')  # time at next scr refresh
        Image3.setAutoDraw(True)
    
    # *Image4* updates
    if Image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Image4.frameNStart = frameN  # exact frame index
        Image4.tStart = t  # local t and not account for scr refresh
        Image4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Image4, 'tStartRefresh')  # time at next scr refresh
        Image4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['m'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spac4* updates
    if spac4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spac4.frameNStart = frameN  # exact frame index
        spac4.tStart = t  # local t and not account for scr refresh
        spac4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spac4, 'tStartRefresh')  # time at next scr refresh
        spac4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VisualInstrux2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VisualInstrux2"-------
for thisComponent in VisualInstrux2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('headerm.started', headerm.tStartRefresh)
thisExp.addData('headerm.stopped', headerm.tStopRefresh)
thisExp.addData('Image3.started', Image3.tStartRefresh)
thisExp.addData('Image3.stopped', Image3.tStopRefresh)
thisExp.addData('Image4.started', Image4.tStartRefresh)
thisExp.addData('Image4.stopped', Image4.tStopRefresh)
thisExp.addData('spac4.started', spac4.tStartRefresh)
thisExp.addData('spac4.stopped', spac4.tStopRefresh)
# the Routine "VisualInstrux2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Practice"-------
continueRoutine = True
# update component parameters for each repeat
Practiceresponse.keys = []
Practiceresponse.rt = []
_Practiceresponse_allKeys = []
# keep track of which components have finished
PracticeComponents = [practice, Practiceresponse, spac5]
for thisComponent in PracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Practice"-------
while continueRoutine:
    # get current time
    t = PracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice* updates
    if practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice.frameNStart = frameN  # exact frame index
        practice.tStart = t  # local t and not account for scr refresh
        practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice, 'tStartRefresh')  # time at next scr refresh
        practice.setAutoDraw(True)
    
    # *Practiceresponse* updates
    waitOnFlip = False
    if Practiceresponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Practiceresponse.frameNStart = frameN  # exact frame index
        Practiceresponse.tStart = t  # local t and not account for scr refresh
        Practiceresponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Practiceresponse, 'tStartRefresh')  # time at next scr refresh
        Practiceresponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Practiceresponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Practiceresponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Practiceresponse.status == STARTED and not waitOnFlip:
        theseKeys = Practiceresponse.getKeys(keyList=['space'], waitRelease=False)
        _Practiceresponse_allKeys.extend(theseKeys)
        if len(_Practiceresponse_allKeys):
            Practiceresponse.keys = _Practiceresponse_allKeys[-1].name  # just the last key pressed
            Practiceresponse.rt = _Practiceresponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *spac5* updates
    if spac5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spac5.frameNStart = frameN  # exact frame index
        spac5.tStart = t  # local t and not account for scr refresh
        spac5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spac5, 'tStartRefresh')  # time at next scr refresh
        spac5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice"-------
for thisComponent in PracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice.started', practice.tStartRefresh)
thisExp.addData('practice.stopped', practice.tStopRefresh)
thisExp.addData('spac5.started', spac5.tStartRefresh)
thisExp.addData('spac5.stopped', spac5.tStopRefresh)
# the Routine "Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracticeList = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Sample_Task_MRT.xlsx'),
    seed=None, name='PracticeList')
thisExp.addLoop(PracticeList)  # add the loop to the experiment
thisPracticeList = PracticeList.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeList.rgb)
if thisPracticeList != None:
    for paramName in thisPracticeList:
        exec('{} = thisPracticeList[paramName]'.format(paramName))

for thisPracticeList in PracticeList:
    currentLoop = PracticeList
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeList.rgb)
    if thisPracticeList != None:
        for paramName in thisPracticeList:
            exec('{} = thisPracticeList[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    win.mouseVisible = False
    # keep track of which components have finished
    fixationComponents = [fixa]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixa* updates
        if fixa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixa.frameNStart = frameN  # exact frame index
            fixa.tStart = t  # local t and not account for scr refresh
            fixa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixa, 'tStartRefresh')  # time at next scr refresh
            fixa.setAutoDraw(True)
        if fixa.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixa.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixa.tStop = t  # not accounting for scr refresh
                fixa.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixa, 'tStopRefresh')  # time at next scr refresh
                fixa.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeList.addData('fixa.started', fixa.tStartRefresh)
    PracticeList.addData('fixa.stopped', fixa.tStopRefresh)
    
    # ------Prepare to start Routine "StimDisplay"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(ImageFile1)
    image_4.setImage(ImageFile2)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    win.mouseVisible = False
    # keep track of which components have finished
    StimDisplayComponents = [image_3, image_4, key_resp]
    for thisComponent in StimDisplayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StimDisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StimDisplay"-------
    while continueRoutine:
        # get current time
        t = StimDisplayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StimDisplayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['x', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimDisplayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StimDisplay"-------
    for thisComponent in StimDisplayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeList.addData('image_3.started', image_3.tStartRefresh)
    PracticeList.addData('image_3.stopped', image_3.tStopRefresh)
    PracticeList.addData('image_4.started', image_4.tStartRefresh)
    PracticeList.addData('image_4.stopped', image_4.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for PracticeList (TrialHandler)
    PracticeList.addData('key_resp.keys',key_resp.keys)
    PracticeList.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        PracticeList.addData('key_resp.rt', key_resp.rt)
    PracticeList.addData('key_resp.started', key_resp.tStartRefresh)
    PracticeList.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "StimDisplay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    if key_resp.corr == 1:
        msg = "Congratulations!"
    else:
        msg = "Oops! That was incorrect."
    show.setText(msg)
    text_7.setText(corrAnsText)
    space.keys = []
    space.rt = []
    _space_allKeys = []
    answered.setText('You answered:')
    answer.setText(key_resp.keys)
    # keep track of which components have finished
    FeedbackComponents = [show, text_7, space, text_8, answered, answer]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *show* updates
        if show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            show.frameNStart = frameN  # exact frame index
            show.tStart = t  # local t and not account for scr refresh
            show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(show, 'tStartRefresh')  # time at next scr refresh
            show.setAutoDraw(True)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *space* updates
        waitOnFlip = False
        if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space.frameNStart = frameN  # exact frame index
            space.tStart = t  # local t and not account for scr refresh
            space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
            space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space.status == STARTED and not waitOnFlip:
            theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
            _space_allKeys.extend(theseKeys)
            if len(_space_allKeys):
                space.keys = _space_allKeys[-1].name  # just the last key pressed
                space.rt = _space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        
        # *answered* updates
        if answered.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answered.frameNStart = frameN  # exact frame index
            answered.tStart = t  # local t and not account for scr refresh
            answered.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answered, 'tStartRefresh')  # time at next scr refresh
            answered.setAutoDraw(True)
        
        # *answer* updates
        if answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            answer.frameNStart = frameN  # exact frame index
            answer.tStart = t  # local t and not account for scr refresh
            answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
            answer.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeList.addData('show.started', show.tStartRefresh)
    PracticeList.addData('show.stopped', show.tStopRefresh)
    PracticeList.addData('text_7.started', text_7.tStartRefresh)
    PracticeList.addData('text_7.stopped', text_7.tStopRefresh)
    PracticeList.addData('text_8.started', text_8.tStartRefresh)
    PracticeList.addData('text_8.stopped', text_8.tStopRefresh)
    PracticeList.addData('answered.started', answered.tStartRefresh)
    PracticeList.addData('answered.stopped', answered.tStopRefresh)
    PracticeList.addData('answer.started', answer.tStartRefresh)
    PracticeList.addData('answer.stopped', answer.tStopRefresh)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeList'


# ------Prepare to start Routine "Start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
StartComponents = [text3, key_resp_5, text_5]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text3* updates
    if text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text3.frameNStart = frameN  # exact frame index
        text3.tStart = t  # local t and not account for scr refresh
        text3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text3, 'tStartRefresh')  # time at next scr refresh
        text3.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text3.started', text3.tStartRefresh)
thisExp.addData('text3.stopped', text3.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TrialList1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_and_Correct_Answers_Part_1.xlsx'),
    seed=None, name='TrialList1')
thisExp.addLoop(TrialList1)  # add the loop to the experiment
thisTrialList1 = TrialList1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialList1.rgb)
if thisTrialList1 != None:
    for paramName in thisTrialList1:
        exec('{} = thisTrialList1[paramName]'.format(paramName))

for thisTrialList1 in TrialList1:
    currentLoop = TrialList1
    # abbreviate parameter names if possible (e.g. rgb = thisTrialList1.rgb)
    if thisTrialList1 != None:
        for paramName in thisTrialList1:
            exec('{} = thisTrialList1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    win.mouseVisible = False
    # keep track of which components have finished
    fixationComponents = [fixa]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixa* updates
        if fixa.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixa.frameNStart = frameN  # exact frame index
            fixa.tStart = t  # local t and not account for scr refresh
            fixa.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixa, 'tStartRefresh')  # time at next scr refresh
            fixa.setAutoDraw(True)
        if fixa.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixa.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixa.tStop = t  # not accounting for scr refresh
                fixa.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixa, 'tStopRefresh')  # time at next scr refresh
                fixa.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TrialList1.addData('fixa.started', fixa.tStartRefresh)
    TrialList1.addData('fixa.stopped', fixa.tStopRefresh)
    
    # ------Prepare to start Routine "StimDisplay1"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(ImageFile1)
    image_2.setImage(ImageFile2)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    StimDisplay1Components = [image, image_2, key_resp_7]
    for thisComponent in StimDisplay1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StimDisplay1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "StimDisplay1"-------
    while continueRoutine:
        # get current time
        t = StimDisplay1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StimDisplay1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['x', 'm'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[0].name  # just the first key pressed
                key_resp_7.rt = _key_resp_7_allKeys[0].rt
                # was this correct?
                if (key_resp_7.keys == str(corrAns)) or (key_resp_7.keys == corrAns):
                    key_resp_7.corr = 1
                else:
                    key_resp_7.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StimDisplay1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "StimDisplay1"-------
    for thisComponent in StimDisplay1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TrialList1.addData('image.started', image.tStartRefresh)
    TrialList1.addData('image.stopped', image.tStopRefresh)
    TrialList1.addData('image_2.started', image_2.tStartRefresh)
    TrialList1.addData('image_2.stopped', image_2.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_7.corr = 1;  # correct non-response
        else:
           key_resp_7.corr = 0;  # failed to respond (incorrectly)
    # store data for TrialList1 (TrialHandler)
    TrialList1.addData('key_resp_7.keys',key_resp_7.keys)
    TrialList1.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        TrialList1.addData('key_resp_7.rt', key_resp_7.rt)
    TrialList1.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    TrialList1.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "StimDisplay1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'TrialList1'


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
GoodbyeComponents = [Final, key_resp_6, text_6]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Final* updates
    if Final.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Final.frameNStart = frameN  # exact frame index
        Final.tStart = t  # local t and not account for scr refresh
        Final.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Final, 'tStartRefresh')  # time at next scr refresh
        Final.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Final.started', Final.tStartRefresh)
thisExp.addData('Final.stopped', Final.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
