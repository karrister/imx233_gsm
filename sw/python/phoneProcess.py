#!/usr/bin/python
# Author: 
#    Karri Kivelä
#
# Description:
#    This is the main file for the Python mobile phone application.
# This file is ran and manages the interfacing of the Hardware as
# well as the other Python components.

from modemATParser import ATParser
from keyPad import Keypad
from busDriver import BusDriver
from screen import Screen
from SIM900 import SIM900

def mainPhoneProcess(modem, bus, keypad, screen):

    parser = ATParser()
    noErrorDetected = True

    while noErrorDetected == True:

        if modem.isChipInErrorState() == True:
            noErrorDetected = False

        if keypad.isUserActionWaiting():

            userAction = keypad.getUserAction()
            screen.updateScreen(userAction)
            rawATResponse = parser.buildATResponseForAction(userAction)
            bus.syncWrite(rawATResponse)
        
        rawATCommand = bus.syncRead()
        parsedAction = parser.parseATCommand(rawATCommand)
        screen.updateScreen(parsedAction)
        rawATResponse = parser.buildATResponseForAction(parsedAction)
        bus.syncWrite(rawATResponse)
    #Loop while noErrorDetected


def phoneStart();

    bus = BusDriver()

    while bus.isBusInitialized() == False:

        if bus.isBusInErrorState() == True:
            #Well, this was unexpected... We should return
            #from the app. Or maybe attempt a reset?
            return

    modem = SIM900(bus) #Constructor starts the Chip init

    while modem.isChipInitialized() == False:
        
        if modem.isChipInErrorState() == True:
            #Well, this was unexpected... We should return
            #from the app. Or maybe attempt a reset?
            return

    keypad = Keypad()
    if keypad.isInErrorState() == True:
        return

    screen = Screen()
    if screen.isInErrorState() == True:
        return

    #Init is complete, turn into the main part of the app
    #This call will be blocking for the lifetime of the app
    #and return only after an error was detected
    mainPhoneProcess(modem, bus, keypad, screen)




