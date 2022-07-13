import os
from threading import Thread
import pyautogui as gui
import time

def launch_mytoolkit():
    gui.hotkey("ctrl","alt","t")
    time.sleep(3)
    gui.typewrite('nodemon ~/Desktop/mytoolkit/server.js')
    gui.typewrite(["enter"])
    time.sleep(3)
    Thread(target=os.system,args=("google-chrome",)).start()
    time.sleep(3)
    gui.moveTo(547,93)
    gui.click()
    gui.typewrite("http://localhost:5011")
    gui.typewrite(["enter"])
    gui.moveTo(1347,93)
    gui.click()
    gui.moveTo(1332,303)
    gui.click()
    time.sleep(2)

    
