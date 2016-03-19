#!/usr/bin/python
# Author: 
#    Karri Kivelä
#
# Description:
#    This is the comms bus driver, in
# this case the UART driver that takes
# care of communication with the Chip.

class BusDriver:

    isBusInitialized = False
    isBusInErrorState = False

    #Currently the constructor will do a blocking init,
    #returning to the user only after Chip is up
    def __init__(self, isBlockingInit = True):
        
        #TODO: remove this state change if implement non Blocking constructor
        isBusInitialized = True
        
    def isBusInitialed(self):
        return self.isBusInitialized

    def isBusInErrorState(self):
        return self.isBusInErrorState

    def syncRead(self):
        #stub for a blocking UART read until end of AT command










