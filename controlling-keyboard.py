#! python3

import pyautogui

pyautogui.click(100, 100)

pyautogui.typewrite('hello world', interval=0.2)

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

pyautogui.hotkey('ctrl', 'o')