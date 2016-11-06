#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the comms bus driver, in
# this case the UART driver that takes
# care of communication with the Chip.

import serial

READ_TIMEOUT_SECS = 2
BAUDRATE = 19200
#Serial has different pointer in different OS and board
SERIAL_DEV_NAME = "COM20" #Windows
#SERIAL_DEV_NAME = "/dev/ttyAPP0" #Linux imx233

class BusDriver:

	isBusInitialized = False
	isBusInErrorState = False
	busContext = serial.Serial()

	#Currently the constructor will do a blocking init,
	#returning to the user only after Chip is up
	def __init__(self, log, isBlockingInit = True):
		self.log = log
		busContext = self.openBus()
		#TODO: remove this state change if implement non Blocking constructor
		isBusInitialized = True

	def isBusInitialized(self):
		return self.isBusInitialized

	def isBusInErrorState(self):
		return self.isBusInErrorState
		
	def openBus(self):
		try:
			self.busContext = serial.Serial()
			self.busContext.port = SERIAL_DEV_NAME
			self.busContext.timeout = READ_TIMEOUT_SECS
			self.busContext.baudrate = BAUDRATE
			self.busContext.open()
			isBusInitialized = True
		except serial.serialutil.SerialException:
			self.log.pushLogMsg("We got an exception attempting to open the serial!")
			self.closeBus()
			return
		
	def closeBus(self):
		isBusInitialized = False
		self.busContext.close()

	#Blocking read
	def syncRead(self):
	
		if self.isBusInitialized() == False or self.isBusInErrorState() == True:
			return
	
		try:
			#time.sleep(READ_TIMEOUT_SECS)
			busContext_string = self.busContext.readline()
			
			self.log.pushLogMsg("UART_R: " + busContext_string, 255)
		except serial.serialutil.SerialException:
			self.log.pushLogMsg("We got an exception from the serial!")
			self.closeBus()
			return
			
		return busContext_string

	#Blocking write
	def syncWrite(self, uartString):
		
		if self.isBusInitialized() == False or self.isBusInErrorState() == True:
			return
			
		self.log.pushLogMsg("UART_W: " + uartString, 255)
			
		try:
			self.busContext.write(uartString)
		except serial.serialutil.SerialException:
			self.log.pushLogMsg("We got an exception from the serial!")
			self.closeBus()
			return








