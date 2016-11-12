import time
import serial

AT_CMD_ECHO_ENABLE = b'ATE1\r\n'
AT_CMD_ECHO_DISABLE = b'ATE0\r\n'
AT_CMD_QUERY_NET_STATUS = b'AT+CREG?\r\n'
AT_CMD_QUERY_STATUS = b'AT\r\n'

CREG_NETWORK_UP_STATUSES = (1 << 5 | 1 << 1) # 5 = registered, roaming. 1 = registered, home network

IC_OK_TIMEOUT_SECS = 10
GSM_NETWORK_CONN_TIMEOUT_SECS = 120
READ_TIMEOUT_SECS = 2
BAUDRATE = 19200
#Serial has different pointer in different OS and board
SERIAL_DEV_NAME = "COM20" #Windows
#SERIAL_DEV_NAME = "/dev/ttyAPP0" #Linux imx233

def disable_uart_echo_mode():
	
	print "Disabling echoing of written UART characters..."
	
	com = serial.Serial()
	com.port = SERIAL_DEV_NAME
	com.timeout = READ_TIMEOUT_SECS
	com.baudrate = BAUDRATE
	com.open()
	
	try:
		com.write(AT_CMD_ECHO_DISABLE)
	except serial.serialutil.SerialException:
		print "We got an exception from the serial!"
		com.close()
		
def enable_uart_echo_mode():
	
	print "Enabling echoing of written UART characters..."
	
	com = serial.Serial()
	com.port = SERIAL_DEV_NAME
	com.timeout = READ_TIMEOUT_SECS
	com.baudrate = BAUDRATE
	com.open()
	
	try:
		com.write(AT_CMD_ECHO_ENABLE)
	except serial.serialutil.SerialException:
		print "We got an exception from the serial!"
		com.close()

def check_chip_in_ok_state():

	print "Starting to test connectivity with the Chip..."
	
	secs_passed = 0
	
	com = serial.Serial()
	com.port = SERIAL_DEV_NAME
	com.timeout = READ_TIMEOUT_SECS
	com.baudrate = BAUDRATE
	com.open()
	
	print "Testing that Chip is in OK state"
	
	while secs_passed < IC_OK_TIMEOUT_SECS:
		try:
			com.write(AT_CMD_QUERY_STATUS)
			time.sleep(READ_TIMEOUT_SECS)
			com_string = com.readline()
			print com_string
		except serial.serialutil.SerialException:
			print "We got an exception from the serial!"
			com.close()

		if com_string[:2] == "OK":
			print "The Chip is up and running!"
			break			
		
		secs_passed = secs_passed + READ_TIMEOUT_SECS
		print "| ",secs_passed," secs |"

	
	com.close()
	
def check_network_connection():
	
	print "Starting to test connectivity status with the GSM provider"
	
	secs_passed = 0
	gsm_connected = False
	
	com = serial.Serial()
	com.port = SERIAL_DEV_NAME
	com.timeout = READ_TIMEOUT_SECS
	com.baudrate = BAUDRATE
	com.open()
	
	while secs_passed < GSM_NETWORK_CONN_TIMEOUT_SECS:
	
		try:
			com.write(AT_CMD_QUERY_NET_STATUS)
			time.sleep(READ_TIMEOUT_SECS)
			com_string = com.readline()
			print com_string
		except serial.serialutil.SerialException:
			print "We got an exception from the serial!"
			com.close()
		
		if com_string[:6] == "+CREG:":
			net_status_bm = 1 << int(com_string[(com_string.index(','))+1:])
			
			if net_status_bm & CREG_NETWORK_UP_STATUSES:
				print "The board is successfully connected to a GSM network!"
				break
				
		secs_passed = secs_passed + READ_TIMEOUT_SECS
		print "| ",secs_passed," secs |"
	

if __name__ == "__main__":
	
	disable_uart_echo_mode()
	check_chip_in_ok_state()
	check_network_connection()
	enable_uart_echo_mode()

