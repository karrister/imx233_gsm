IMX233 GSM
=============

This project started as my thesis project for the University (of applied sciences) of Helsinki. The project is about making a simple open source, Linux based cellular phone. In the heart of the device are an Olimex made Olinuxino (the original) IMX233 development board, connected over an application UART to a SIM900 GPRS GSM-development board. I will also connect a self-made keypad (1 button at first stage) and a self-made screen (1 LED indicator at first stage).

For now I have seized the PCB design for a board combining the two Chips on a shared board, as the final design did not meet the requirements for printing. I will publish the current PCB design files (kicad) here and also plan to continue the work to have a printed board eventually.

Currently I have created a 4.1.1 kernel, running with Debian Jessie on the CPU. The Software for interfacing the Hardware will be a set of Python scripts, communicating with the Chip, parsing the AT commands as well as controlling the custom keypad and screen.
