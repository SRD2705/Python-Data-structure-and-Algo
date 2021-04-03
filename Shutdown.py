import os
import pyautogui as pe
import time
import subprocess
time.sleep(1)
os.startfile('C:/Users/Hp/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad')
time.sleep(1)  # Here 1 is the tome to reach location; You can edit it.
pe.typewrite("Hi Rishi\nI will take care from here\nSee you soon sir, Hail Python! :) \nShutting down in 5 seconds...",0.1) # 0.1 is the typing speed
pe.typewrite("\n* * * * *",1)
pe.hotkey('alt','f4')
time.sleep(1)
pe.press('tab')
time.sleep(1)
pe.press('enter')
pe.moveTo(29,1058,1)
pe.click(29,1058)
pe.moveTo(33,991,1.2)
pe.click(33,991)
pe.moveTo(85,895,1)
pe.click(85,895)
