#! python3

import pyautogui

width, height = pyautogui.size()

pyautogui.position()

pyautogui.moveTo(10, 10, duration=1.5)

pyautogui.moveRel(200, 0, duration=2)

pyautogui.displayMousePosition()