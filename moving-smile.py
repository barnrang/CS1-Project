# moving-smile.py
# Output: Moving smiley
import time
import os
from pynput.keyboard import Key, Controller, Listener
clear = lambda : os.system('clear')


L = 28

img0 = 0000000000000000000000000000
img1 = 0000000000000000000000000000
img2 = 0000000000000000000000000000
img3 = 0000000000000000000000000000
img4 = 0000000000000000000000000000
img5 = 0000000000000000000000000000
img6 = 0000000000000000000000000000
img7 = 0000000000000000000000000000
img8 = 0000000000000000000000000000
img9 = 0000000000000000000000000000
pos1 = 1100000000000000000000000000
pos2 = 1100000000000000000000000000
verti = 8

output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]


t = 0
def on_press(key):
    global verti, pos1, pos2
    
    if key == Key.alt:
        verti = max(verti - 1, 0)
        print(verti)
        print('hello')
    elif key == Key.cmd:
        verti = min(8, verti + 1)
    
    elif key == Key.alt_r:
        pos1 = max(11, pos1//10)
        pos2 = max(11, pos2//10)
    
    elif key == Key.cmd_r:
        pos1 = min(1100000000000000000000000000, pos1 * 10)
        pos2 = min(1100000000000000000000000000, pos2 * 10)


def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

def render():
    copy_array = [x for x in output_array]
    copy_array[verti] += pos1
    copy_array[verti + 1] += pos2
    for line in copy_array:
        print('{0:028d}'.format(line))

with Listener(on_press=on_press, on_release=on_release) as listener:

    while t < 1000:

        render()
        time.sleep(0.1)
        clear()
        t += 1
        print(verti)
#        print(t)

    listener.join()
