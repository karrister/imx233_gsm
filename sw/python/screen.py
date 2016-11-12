#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for controlling the screen

class Screen:

	isInErrorState = False
	ledState = False
	currentScreenText = ""
	idleText = ""

	def __init__(self, log):
		
		self.turnLedOff()
		self.ledState = False
		self.setScreenText("Init...")
		self.setScreenIdleText("imx233_phone") #default idle text
		self.log = log

	def isInErrorState(self):
		return self.isInErrorState
		
	def turnLedOn(self):
		#TODO: write to HW
		self.ledState = True
	
	def turnLedOff(self):
		#TODO: write to HW
		self.ledState = False
		
	def setScreenText(self, string):
		#TODO: write to HW
		self.currentScreenText = string
		
	def setScreenIdleText(self, string):
		self.idleText = string
		

	def updateScreen(self, action):
		
		if action.incomingCall == True and action.hasUserAnsweredCall == False:
			self.setScreenText("Ringing")
			
		if action.incomingCall == True and action.hasUserAnsweredCall == True:
			self.setScreenText("Answered")

		if action.incomingCall == False and action.hasUserAnsweredCall == False:
			self.setScreenText(self.idleText)
			
