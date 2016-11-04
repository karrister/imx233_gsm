#!/usr/bin/python
# Author: 
#    Karri Kivela
#
# Description:
#    This is the file for actions.

class Action:

    isInErrorState = False
	#nextAction = 
	incomingCall = False
	hasUserAnsweredCall = False
	noCommand = True
	userDialedCall = False
	userDialedNumber = "0587155100"
	

    def __init__(self):
        print "Only a stub for now"

	def setDialToNumber(self, numberString):
		self.userDialedNumber = numberString

	def getDialToNumber(self):
		return self.userDialedNumber