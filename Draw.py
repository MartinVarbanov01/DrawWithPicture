import math
import time
from PIL import Image
import pyautogui
from pynput.mouse import Listener
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def hold(x, y, d):
    win32api.SetCursorPos((x, y))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.SetCursorPos((x + d, y))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


img = Image.open(input("Name the image: "))
im = img.convert("L")
# im.save("f.png")
xImg, yImg = im.size
draw_once = True
shades = [764, 784, 807, 829, 853, 874, 892, 913, 935, 957]
set_sh = False
if input("Do you want to set the shades y/n:") == "y":
    set_sh = True

pv = list(im.getdata())
temp = []
pixels = [[], [], [], [], [], [], [], [], [], []]
count_pixels = 0
count_shades = 0
old_item = 500


def place(lum):
    global temp, pixels
    if lum < 25:
        pixels[0].append(temp)
    elif lum < 50:
        pixels[1].append(temp)
    elif lum < 75:
        pixels[2].append(temp)
    elif lum < 100:
        pixels[3].append(temp)
    elif lum < 125:
        pixels[4].append(temp)
    elif lum < 150:
        pixels[5].append(temp)
    elif lum < 175:
        pixels[6].append(temp)
    elif lum < 200:
        pixels[7].append(temp)
    elif lum < 225:
        pixels[8].append(temp)
    elif lum < 250:
        pixels[9].append(temp)


def right(old, new):
    if old in range(0, 25) and new in range(0, 25):
        return True
    if old in range(25, 50) and new in range(25, 50):
        return True
    if old in range(50, 75) and new in range(50, 75):
        return True
    if old in range(75, 100) and new in range(75, 100):
        return True
    if old in range(100, 125) and new in range(100, 125):
        return True
    if old in range(125, 150) and new in range(125, 150):
        return True
    if old in range(150, 175) and new in range(150, 175):
        return True
    if old in range(175, 200) and new in range(175, 200):
        return True
    if old in range(200, 225) and new in range(200, 225):
        return True
    if old in range(225, 250) and new in range(225, 250):
        return True
    return False


old_x = 0
old_y = 0
for item in pv:
    cord_x = (count_pixels % xImg + 1)
    cord_y = math.floor(count_pixels / xImg)
    if right(old_item, item) and cord_x < xImg:
        count_shades += 1
    else:
        temp = [old_x - count_shades, old_y, count_shades, old_item]
        if old_item != 500:
            place(old_item)
        else:
            place(item)
        count_shades = 0
    old_item = item
    old_x = cord_x
    old_y = cord_y
    count_pixels += 1
# print(pixels[0])


def set_shades(set_shade):
    if set_shade:
        color = 0
        for i in range(10):
            click(980, 105)
            time.sleep(0.5)
            click(1075, 638)
            click(1075, 638)
            time.sleep(0.5)
            pyautogui.write(str(color))
            color += 25
            click(773, 664)
            time.sleep(0.5)


def on_click(x, y, button, pressed):
    global pv, xImg, yImg, draw_once, im, pixels, set_sh
    if pressed and draw_once and str(button) == "Button.left":
        draw_once = False
        set_shades(set_sh)
        time.sleep(1)
        for i in range(10):
            click(shades[i], 105)
            for pixel in pixels[i]:
                hold(pixel[0] + x, pixel[1] + y, pixel[2])
        exit()


with Listener(on_click=on_click) as listener:
    listener.join()
