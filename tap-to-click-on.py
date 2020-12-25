#!/usr/bin/python3
# change the line above if your python 3 executable is somewhere else
# -
# This python script turns touchpad tap-to-click on in libinput-xinput
# on my system the property number varies if a mouse is connected, so using a simple xinput shell commend did not work for me
import os

# obtaining the touchpad name
lines = os.popen('xinput -list')
touchpad_name = ""
for line in lines:
    if 'Touchpad' in line:
        for char in line:
            touchpad_name += char
            if 'Touchpad' in touchpad_name:
                break
touchpad_name = touchpad_name.strip('⎜   ↳ ')

# assign touchpad name
TOUCHPAD_NAME = touchpad_name
#TOUCHPAD_NAME = 'ELAN0504:00 04F3:3091 Touchpad'      # static version; useful if more than one touchpad available

# obtaining the property number
lines = os.popen('xinput --list-props "' + TOUCHPAD_NAME + '"')
for line in lines:
    if 'Tapping Enabled (' in line:
        # find property number
        property_number = ""
        for char in line:
            property_number += char
            if char == '(':
                property_number = ""
            elif char == ')':
                property_number = property_number.strip(')')
                break
        break
os.system('xinput --set-prop "' + TOUCHPAD_NAME + '" ' + property_number + ' 1')
