#!/usr/bin/python
# Author: 
#    Karri Kivela
#
# Description:
#    This is the file for controlling the screen

class Screen:

    isInErrorState = False

    def __init__(self):
        print "Only a stub for now"

    def isInErrorState(self):
        return self.isInErrorState

    def updateScreen(self, action):
        
		if action.incomingCall == True and action.hasUserAnsweredCall == False:
			#Update screen for incoming call state
			
		if action.incomingCall == True and action.hasUserAnsweredCall == True:
			#Update screen for incoming call state that was answered

		if action.incomingCall == False and action.hasUserAnsweredCall == False:
			#Update screen for idle state