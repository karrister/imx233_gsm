#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for actions.

class Action:

	isInErrorState = False
	#nextAction = 
	incomingCall = False
	hasUserAnsweredCall = False
	noCommand = False
	userDialedCall = False
	userDialedNumber = "0587155100" #For now the phone number
	callDisconnected = False

	#def __init__(self):
	#nothing

	def setDialToNumber(self, numberString):
		self.userDialedNumber = numberString

	def getDialToNumber(self):
		return self.userDialedNumber