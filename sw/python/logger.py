#!/usr/bin/python
# Author: 
#	Karri Kivela
#
# Description:
#	This is the file for logging the operation.

LOG_INFO = 0

class Logger:

	isInErrorState = False	

	def __init__(self):
		print "For now the logger supports only printing the message"
		
		
	def pushLogMsg(string, verbosity = LOG_INFO):
		print "TODO: fix logger" #"V" + verbosity + ": " + string

	
