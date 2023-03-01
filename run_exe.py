import subprocess, sys
import pyautogui
import time

from subprocess import Popen, PIPE
from turtle import forward, screensize

exe_str = r"C:\Users\Kevin.Jurina\Downloads\vlc-3.0.18-win32.exe"

parent = subprocess.Popen(exe_str, stderr=subprocess.PIPE)

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
screenWidth, screenHeight
(1920, 1080)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
currentMouseX, currentMouseY
(1314, 345)

pyautogui.moveTo(940, 565) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(940, 565)

#res = pyautogui.locateOnScreen("vlc_weiter.png")
#print(res)

#res = pyautogui.locateCenterOnScreen("vlc_weiter.png")
#print(res)

pyautogui.press("enter", presses = 4, interval= 2.5)

time.sleep(10)  

pyautogui.hotkey("enter")

print("VLC player is now installed")
