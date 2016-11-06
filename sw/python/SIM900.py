#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for SIM900 specific logic, such as
# having the init logic of the Chip, and possible customized
# AT commands parsing.


AT_CMD_ECHO_ENABLE = b'ATE1\r\n'
AT_CMD_ECHO_DISABLE = b'ATE0\r\n'

class SIM900:

	isChipInitialized = False
	isChipInErrorState = False

	#Currently the constructor will do a blocking init,
	#returning to the user only after Chip is up
	def __init__(self, bus, log, isBlockingInit = True):
		self.log = log
		self.bus = bus
		
		#TODO: do chip init
		
		#TODO: remove this state change if implement non Blocking constructor
		isChipInitialized = True
		
	def isChipInitialized(self):
		return self.isChipInitialized

	def isChipInErrorState(self):
		return self.isChipInErrorState

	def disable_uart_echo_mode(self):
			
		self.log.pushLogMsg("Disabling echoing of written UART characters...", 255)
		
		self.bus.syncWrite(AT_CMD_ECHO_DISABLE)
			
	def enable_uart_echo_mode(self):
		
		self.log.pushLogMsg("Enabling echoing of written UART characters...", 255)
		
		self.bus.syncWrite(AT_CMD_ECHO_ENABLE)
			
