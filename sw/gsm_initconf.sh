#! /bin/sh
### BEGIN INIT INFO
# Provides:          gsm_initconf
# Required-Start:    $all
# Required-Stop:
# Should-Start:
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Run init config related to GSM board
# Description:       Runs the init related to GSM board, setting
#                    up the GPIO and blinking startup LED test.
### END INIT INFO
echo 91 > /sys/class/gpio/export
echo 92 > /sys/class/gpio/export
echo out >/sys/class/gpio/gpio91/direction
echo in >/sys/class/gpio/gpio92/direction
echo 0 >/sys/class/gpio/gpio92/value
echo 1 >/sys/class/gpio/gpio91/value
sleep 4
echo 0 >/sys/class/gpio/gpio91/value
sleep 1
echo 1 >/sys/class/gpio/gpio91/value
sleep 1
echo 0 >/sys/class/gpio/gpio91/value
sleep 1
echo 1 >/sys/class/gpio/gpio91/value
sleep 1
echo 0 >/sys/class/gpio/gpio91/value
sleep 10
python /root/gsm/phoneProcess.py
