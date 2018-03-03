#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for knowing the device state between SW modules.


class State:

	isInErrorState = False
	userActionWaiting = False
	incomingCall = False
	hasUserAnsweredCall = False
	userDialedCall = False
	userDialedNumber = "0587155100" #For now the phone number
	connectedCall = False
	userDisconnected = False

	def __init__(self, log):

		self.log = log