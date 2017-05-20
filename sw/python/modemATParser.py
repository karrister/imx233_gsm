#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the main AT commands parser, and the
# response builder.

from action import Action
from logger import Logger

##################
#AT commands list#
##################
AT_CMD_ANSWER_CALL = b'ATA'
AT_CMD_DIAL_CALL = b'ATD'
AT_CMD_EOL = b'\r\n'

##################
##################

class ATParser:

	def __init__(self, screen, keypad, bus, modem, log):
		self.screen = screen
		self.keypad = keypad
		self.bus = bus
		self.modem = modem
		self.log = log
	
	def parseATCommand(self, rawATCommand):
	
		action = Action()
		
		#We don't know yet if we have parser implemented for this AT command,
		#set error state for now
		action.noCommand = True
		
		if not isinstance(rawATCommand, str):
			action.isInErrorState = True
			return action
		
		if rawATCommand[:4] == "RING":
			action.incomingCall = True
			action.isInErrorState = False
			action.noCommand = False
			self.log.pushLogMsg("Incoming call")

		if rawATCommand[:10] == "NO CARRIER" or rawATCommand[:9] == "NO ANSWER":
			action.incomingCall = False
			action.isInErrorState = False
			action.noCommand = False
			self.log.pushLogMsg("Call disconnected")
			
		
		if action.noCommand == True:
			self.log.pushLogMsg(("AT parser failed to parse the AT command: " + rawATCommand)) #rawATCommand.toString()))
			
		return action

	def buildATResponseForAction(self, action):
		
		if action.incomingCall == True and action.hasUserAnsweredCall == True:
			return AT_CMD_ANSWER_CALL + AT_CMD_EOL
			
		if action.userDialedCall == True:
			return AT_CMD_DIAL_CALL + action.getDialToNumber() + ";"  + AT_CMD_EOL #semicolon after dial number

		

