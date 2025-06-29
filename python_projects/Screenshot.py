import pyautogui
import time

def screeshot():
    time.sleep(5)
    name = time.time()
    name = 'D:/Python_programming_course/python_projects/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()
screeshot()