import serial # add Serial library for serial communication
import pyautogui # add pyautogui library for

#programmatically controlling the mouse and keyboard. 

Arduino_Serial = serial.Serial('com12',9600) # Initialize serial and Create
#Serial port object called Arduino_Serial

while 1:
  incoming_data = str (Arduino_Serial.readline())     # read the serial data and print it as line
  print incoming_data                                 # print the incoming Serial data
  
  if 'next' in incoming_data:                         # if incoming data is 'next' 
    pyautogui.hotkey('ctrl', 'right')                 # perform "ctrl+right" operation which forwards the video
    
  if 'previous' in incoming_data:                     # if incoming data is 'previous' 
    pyautogui.hotkey('ctrl', 'left')                  # perform "ctrl+left" operation which rewinds the video
    
  if 'down' in incoming_data:                         # if incoming data is 'down' 
     pyautogui.hotkey(‘ctrl’,'down')                  # performs "ctrl+down arrow" # operation which reduces the volume
  
  if 'up' in incoming_data:                           # if incoming data is 'up' 
    pyautogui.hotkey(‘ctrl’+'up')                     # performs "up arrow" operation which scrolls up the page
    
  if 'Play/Pause' in incoming_data:                   # if incoming data is  Play/Pause
    puautogui.typewrite([‘space’],0.2 )
    
  incoming_data = "";                                 # clears the data
