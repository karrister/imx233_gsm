#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for controlling the key pad
# and any related logic.

import time

BLOCKING_POLL_TIMEOUT_10S = 10

class Keypad:

	isInErrorState = False
	userActionWaiting = False

	def __init__(self, log):
		#self.isUserActionWaiting = False
		#self.userAction = Action()
		print "Need to implement Class Action!"
		self.log = log

	def isInErrorState(self):
		return self.isInErrorState
		
	def getLatestKeypadState(self):
		#TODO: query the HW
		
		self.userActionWaiting = False
		

	def isUserActionWaiting(self):
		#Currently polls the status only when this func is called.
		#Should be polling and updating in the background
		self.getLatestKeypadState()
		
		return self.userActionWaiting

	def getUserAction(self):
		
		action = Action()
		
		action.userDialedCall = True
		
		return action
		
	#For now, this function blocks for a timeout until user
	#action happens, or the timeout expires
	def waitForUserAction(self, action):
	
		beginning_time = time.time()
		
		exitLoop = False
		
		while exitLoop == False:
			
			if time.time() - beginning_time >= BLOCKING_POLL_TIMEOUT_10S:
				exitLoop = True
				
			#Currently we just assume any user action on keypad means answering the phone.
			#This could easily be extended for wider usage, such as doing another probe to see
			#what user has pressed.
			if self.isUserActionWaiting():
				action.hasUserAnsweredCall = True
				self.log.pushLogMsg("User action on keypad occurred")
				return
				
		#while exitLoop
				
		#No user action occurred
		
		action.hasUserAnsweredCall = False
		#We assume the call is now cut, this is obviously problematic.
		#Should either force hangup, or wait above until we get no carrier.
		action.incomingCall = False
		self.log.pushLogMsg("Waited for user action on keypad but none occurred, call cut")
		return
				
				
				
				
				
				
