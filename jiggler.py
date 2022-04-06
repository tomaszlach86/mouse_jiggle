import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = False
position = pyautogui.position()
while True:
    pyautogui.moveTo(position)
    time.sleep(5)
    pyautogui.moveTo(position.x, position.y+5)
    time.sleep(5)
    pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))


