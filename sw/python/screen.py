#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for controlling the screen

#mock for writing to a temp file
#LED1_FILE_HANDLE = '/tmp/led.txt'
LED1_FILE_HANDLE = '/sys/class/gpio/gpio91/value'

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

		#mock for writing to a temp file
		fd = open(LED1_FILE_HANDLE, 'w')
		fd.write('1')
		fd.close()

		self.ledState = True
	
	def turnLedOff(self):
		#TODO: write to HW

		#mock for writing to a temp file
		fd = open(LED1_FILE_HANDLE, 'w')
		fd.write('0')
		fd.close()

		self.ledState = False
		
	def setScreenText(self, string):
		#TODO: write to HW
		self.currentScreenText = string
		
	def setScreenIdleText(self, string):
		self.idleText = string
		

	def updateScreen(self, action):
		#TODO: update this section, currently this looks like VB/assembly

		if action.incomingCall == True and action.hasUserAnsweredCall == False:
			self.setScreenText("Ringing")
			self.turnLedOn()
			
		if action.incomingCall == True and action.hasUserAnsweredCall == True:
			self.setScreenText("Answered")
			self.turnLedOn()

		if action.userDialedCall == True:
			self.setScreenText("Dialing")
			self.turnLedOn()

		if action.incomingCall == False and action.hasUserAnsweredCall == False and action.userDialedCall == False:
			self.setScreenText(self.idleText)
			self.turnLedOff()
			
