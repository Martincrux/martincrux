import pyautogui
import time


time.sleep(3)

im = pyautogui.screenshot()

t1 = time.time()
x = 45
y = 215
while x <= 990:
    y = 215
    t2 = time.time()
    while y <= 1045:
        t2 = time.time()
        point = im.getpixel((x, y))
        if point[0] <= 5 and point[1] <= 5 and point[2] <= 5:
            print(x, y)
            pyautogui.click(x, y)
            # time.sleep(0.1)
        y = y + 2
        if t2 - t1 >= 30:
            break
    if t2 - t1 >= 30:
        break
    x = x + 2
