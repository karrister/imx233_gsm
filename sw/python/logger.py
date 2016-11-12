#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for logging the operation.

LOG_CRITICAL_ERROR = 1
LOG_ERROR          = 2
LOG_WARNING        = 3
LOG_DEBUG          = 4
LOG_INFO           = 5

LOWEST_LOG_LEVEL_TO_PRINT = LOG_INFO

class Logger:

	isInErrorState = False	

	def __init__(self):
		print "For now the logger supports only printing the message" #ha, not even that because of a bug!
		print "But one can attach logger to write to a file as well, message que, what ever the user wishes"
		
	def pushLogMsg(self, string, verbosity = LOG_INFO):
		if verbosity > LOWEST_LOG_LEVEL_TO_PRINT:
			return
		print "V" + str(verbosity) + ": " + string

	
