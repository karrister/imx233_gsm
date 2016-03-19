#!/usr/bin/python
# Author: 
#    Karri Kivelä
#
# Description:
#    This is the file for controlling the key pad
# and any related logic.

class Keypad:

    isInErrorState = False
    isUserActionWaiting
    userAction

    def __init__(self):
        self.isUserActionWaiting = False
        self.userAction = Action()

    def isInErrorState(self):
        return self.isInErrorState

    def isUserActionWaiting(self):
        #TODO: Do a blocking query of the current status
        return self.isUserActionWaiting

    def getUserAction(self):
        return self.userAction
