
from bs4 import BeautifulSoup
import pyautogui as gui
from time import time, sleep
import json
import requests






def update_domain():
    url = "https://api64.ipify.org/?format=json"
    response = requests.get(url)

    if response.ok:
        
        ip = json.loads(response.content)['ip']
        gui.moveTo(198, 23)
        gui.click()
        sleep(8)
        gui.moveTo(435, 105)
        gui.click()
        gui.typewrite("https://dcc.godaddy.com/manage/desync.in/dns")
        gui.typewrite(["enter"])
        sleep(8)
        gui.moveTo(1361, 229)
        gui.dragTo(1361, 490)
        gui.moveTo(679, 427)
        gui.click()
        sleep(3)
        gui.moveTo(1361, 487)
        gui.dragTo(1361, 387)
        gui.moveTo(1171, 291)
        gui.click()
        gui.moveTo(860, 352)
        gui.click()
        gui.hotkey("ctrl", "a")
        gui.typewrite(ip)
        gui.moveTo(174, 454)
        gui.click()
        gui.sleep(8)
        # for range in (1,60):
        #     gui.typewrite(["tab"])
        gui.moveTo(1347, 59)
        gui.click()
        return "Domain updated sir"
        
    else:
        return "There is some problem in updating domain sir"  

