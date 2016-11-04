#!/usr/bin/python
# Author: 
#    Karri Kivela
#
# Description:
#    This is the file for parsing actions from main process.

from logger import Logger

class ActionParser:

    isInErrorState = False

    def __init__(self, screen, keypad, bus, modem, log):
        self.screen = screen
		self.keypad = keypad
		self.bus = bus
		self.modem = modem
		self.log = log

    def isInErrorState(self):
        return self.isInErrorState
		
	def parseAction(self, action, parser):
		
		#Should not happen
		if action.isInErrorState == True:
			log.pushLogMsg("We are in error state - return from actionParser")
			return
		
		if action.noCommand == True:
			log.pushLogMsg("Not attempting to parse action for a NOP command")
			return
		
		if action.incomingCall == True:
			self.screen.updateScreen(action)
			self.keypad.waitForUserAction(action)
			
			rawATResponse = parser.buildATResponseForAction(userAction)
			self.bus.syncWrite(rawATResponse)
			
			#Update screen again after action
			self.screen.updateScreen(action)
			
		if action.userDialedCall == True:

			self.screen.updateScreen(action)
			
			rawATResponse = parser.buildATResponseForAction(userAction)
			self.bus.syncWrite(rawATResponse)
			
			#Update screen again after action
			self.screen.updateScreen(action)
		
	def screenAction(action):
		print "Is this func needed?"
		#screen.updateScreen(userAction)
        #rawATResponse = parser.buildATResponseForAction(userAction)
        #bus.syncWrite(rawATResponse)
		
	def busAction(action):
		print "Is this func needed?"
		#screen.updateScreen(parsedAction)
        #rawATResponse = parser.buildATResponseForAction(parsedAction)
        #bus.syncWrite(rawATResponse)
	
