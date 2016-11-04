#!/usr/bin/python
# Author: 
#    Karri Kivela
#
# Description:
#    This is the comms bus driver, in
# this case the UART driver that takes
# care of communication with the Chip.

AT_CMD_ECHO_ENABLE = b'ATE1\r\n'
AT_CMD_ECHO_DISABLE = b'ATE0\r\n'
READ_TIMEOUT_SECS = 2
BAUDRATE = 19200
#Serial has different pointer in different OS and board
SERIAL_DEV_NAME = "COM20" #Windows
#SERIAL_DEV_NAME = "/dev/ttyAPP0" #Linux imx233

class BusDriver:

    isBusInitialized = False
    isBusInErrorState = False
	busContext

    #Currently the constructor will do a blocking init,
    #returning to the user only after Chip is up
    def __init__(self, isBlockingInit = True):
        
        #TODO: remove this state change if implement non Blocking constructor
        isBusInitialized = True

    def isBusInitialized(self):
        return self.isBusInitialized

    def isBusInErrorState(self):
        return self.isBusInErrorState
		
	def openBus(self):
		self.busContext = serial.Serial()
		self.busContext.port = SERIAL_DEV_NAME
		self.busContext.timeout = READ_TIMEOUT_SECS
		self.busContext.baudrate = BAUDRATE
		self.busContext.open()
		isBusInitialized = True
		
	def closeBus(self):
		isBusInitialized = False
		self.busContext.close()
		
	def disable_uart_echo_mode(self):
		
		if isBusInitialized() == False or isBusInErrorState() == True:
			return
			
		print "Disabling echoing of written UART characters..."
		
		try:
			self.syncWrite(AT_CMD_ECHO_DISABLE)
		except serial.serialutil.SerialException:
			print "We got an exception from the serial!"
			self.closeBus()
			return
			
	def enable_uart_echo_mode(self):
	
		if isBusInitialized() == False or isBusInErrorState() == True:
			return
		
		print "Enabling echoing of written UART characters..."
				
		try:
			self.syncWrite(AT_CMD_ECHO_ENABLE)
		except serial.serialutil.SerialException:
			print "We got an exception from the serial!"
			self.closeBus()
			return

	#Blocking read
    def syncRead(self):
	
		if isBusInitialized() == False or isBusInErrorState() == True:
			return
	
		try:
			#time.sleep(READ_TIMEOUT_SECS)
			busContext_string = self.busContext.readline()
			#print busContext_string
		except serial.serialutil.SerialException:
			print "We got an exception from the serial!"
			self.closeBus()
			return
			
		return busContext_string

	#Blocking write
    def syncWrite(self, uartString):
        #stub for a blocking UART write
		print "Only a stub for now"
		
		if isBusInitialized() == False or isBusInErrorState() == True:
			return








