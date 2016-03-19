#!/usr/bin/python
# Author: 
#    Karri Kivelä
#
# Description:
#    This is the file for SIM900 specific logic, such as
# having the init logic of the Chip, and possible customized
# AT commands parsing.

class SIM900:

    isChipInitialized = False
    isChipInErrorState = False

    #Currently the constructor will do a blocking init,
    #returning to the user only after Chip is up
    def __init__(self, bus, isBlockingInit = True):
        
        #TODO: remove this state change if implement non Blocking constructor
        isChipInitialized = True
        
    def isChipInitialed(self):
        return self.isChipInitialized

    def isChipInErrorState(self):
        return self.isChipInErrorState
