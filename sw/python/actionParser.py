#!/usr/bin/python
# Author: 
#    Karri Kivela
#
# Description:
#    This is the file for parsing actions from main process.

class ActionParser:

    isInErrorState = False

    def __init__(self):
        print "Only a stub for now"

    def isInErrorState(self):
        return self.isInErrorState
		
	def parseAction(action):
		#do_stuff
		
	def screenAction(action):
		#screen.updateScreen(userAction)
        #rawATResponse = parser.buildATResponseForAction(userAction)
        #bus.syncWrite(rawATResponse)
		
	def busAction(action):
		#screen.updateScreen(parsedAction)
        #rawATResponse = parser.buildATResponseForAction(parsedAction)
        #bus.syncWrite(rawATResponse)
	
