import os
import time
import keyboard
import pyautogui

promptDirect = input('Use default Tello directory? Enter \'y\' or \'n\':  ')
if (promptDirect.casefold() == 'y'):
    directory = 'C:\\Users\\aweso\\OneDrive\\Desktop\\drones\\tello_scratch'
else:
    directory = input('Enter directory location: ')

os.chdir(directory)
time.sleep(2)
print()

#pattern = input('What pattern? Enter \'S\' for Square, \'P\' for Plus, or \'T\' for Triangle:  ')
#if (pattern.casefold() == 's'):
#    pattern = 'C:\\Users\\aweso\\OneDrive\\Desktop\\drones\\tello_scratch\\Square.sb2'
#elif (pattern.casefold() == 'p'):
#    pattern = 'C:\\Users\\aweso\\OneDrive\\Desktop\\drones\\tello_scratch\\Plus.sb2'
#elif (pattern.casefold() == 't'):
#    pattern = 'C:\\Users\\aweso\\OneDrive\\Desktop\\drones\\tello_scratch\\Triangle.sb2'

#os.system(pattern)
#time.sleep(5)
#pyautogui.typewrite('space')

#print()
os.system('node Tello.js')

