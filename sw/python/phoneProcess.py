#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the main file for the Python mobile phone application.
# This file is ran and manages the interfacing of the Hardware as
# well as the other Python components.

from modemATParser import ATParser
from keyPad import Keypad
from busDriver import BusDriver
from screen import Screen
from SIM900 import SIM900
from actionParser import ActionParser
from logger import Logger

def mainPhoneProcess(screen, keypad, bus, modem, logger):

	parser = ATParser(screen, keypad, bus, modem, logger)
	actionParser = ActionParser(screen, keypad, bus, modem, logger)
	noErrorDetected = True

	while noErrorDetected == True:

		if modem.isChipInErrorState() == True:
			noErrorDetected = False

		if keypad.isUserActionWaiting() == True:

			userAction = keypad.getUserAction()
			actionParser.parseAction(userAction)
		
		rawATCommand = bus.syncRead()
		
		#temp hack to make it run
		rawATCommand = ""
		
		parsedAction = parser.parseATCommand(rawATCommand)
		actionParser.parseAction(parsedAction, parser)

		print "DEBUG: Main loop"
	#Loop while noErrorDetected
	
	print "DEBUG: Exit main application"


def phoneStart():

	logger = Logger()

	bus = BusDriver()

	while bus.isBusInitialized() == False:

		if bus.isBusInErrorState() == True:
			#Well, this was unexpected... We should return
			#from the app. Or maybe attempt a reset?
			logger.pushLogMsg("Init: Bus error!")
			return

	modem = SIM900(bus) #Constructor starts the Chip init

	while modem.isChipInitialized() == False:
		
		if modem.isChipInErrorState() == True:
			#Well, this was unexpected... We should return
			#from the app. Or maybe attempt a reset?
			logger.pushLogMsg("Init: Chip error!")
			return

	keypad = Keypad(logger)
	if keypad.isInErrorState() == True:
		logger.pushLogMsg("Init: Keypad error!")
		return

	screen = Screen(logger)
	if screen.isInErrorState() == True:
		logger.pushLogMsg("Init: Screen error!")
		return

	#Init is complete, turn into the main part of the app
	#This call will be blocking for the lifetime of the app
	#and return only after an error was detected
	mainPhoneProcess(screen, keypad, bus, modem, logger)
	
	
if __name__ == "__main__":
	phoneStart()




