# shooting.py
# Output: Dodge the Bullet
import time
import os
import sys
import random
import platform

from pynput.keyboard import Key, Controller, Listener

if platform.system() == 'Windows':
    clear = lambda : os.system('cls')
elif platform.system() == 'Darwin':
    clear = lambda : os.system('clear')

# Global Variable

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
pos1 = 330000000000000
pos2 = 330000000000000
verti = 4
multiplier = 10/23

output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
copy_array = None

t = 0

pressed_key = {
    'w': False,
    's': False,
    'a': False,
    'd': False,
    Key.alt: False,
    Key.alt_r: False,
    Key.cmd: False,
    Key.cmd_r: False
}

bullet_list = []
dead = False
array_copy = False
break_loop = False


def die():
    img0 = 1111100001111111000111111000
    img1 = 1100110001111111000111111000
    img2 = 1100011000011100000110000000
    img3 = 1100011000011100000110000000
    img4 = 1100011000011100000111111000
    img5 = 1100011000011100000111111000
    img6 = 1100011000011100000110000000
    img7 = 1100011000011100000110000000
    img8 = 1100110001111111000111111000
    img9 = 1111100001111111000111111000
    output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    return output_array

def intro1():
    img0 = 1000000000111110000000000000
    img1 = 1000000001111110000000000000
    img2 = 1000000000001110000000000000
    img3 = 1000000000001110000000000000
    img4 = 1000000000001110000000000000
    img5 = 1000000000001110000000000000
    img6 = 1000000000001110000000000000
    img7 = 1000000000001110000000000000
    img8 = 1000000000001110000000000000
    img9 = 1000000000111111100000000000
    output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    return output_array

def intro2():
    img0 = 1000000000111110000000000000
    img1 = 1000000001111111000000000000
    img2 = 1000000011100011100000000000
    img3 = 1000000111000001110000000000
    img4 = 1000000000000011100000000000
    img5 = 1000000000000111000000000000
    img6 = 1000000000001110000000000000
    img7 = 1000000000011100000000000000
    img8 = 1000000000111111100000000000
    img9 = 1000000001111111100000000000
    output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    return output_array

def intro2():
    img0 = 1000000000111110000000000000
    img1 = 1000000001111111000000000000
    img2 = 1000000011100011100000000000
    img3 = 1000000111000001110000000000
    img4 = 1000000000000011100000000000
    img5 = 1000000000000111000000000000
    img6 = 1000000111000011100000000000
    img7 = 1000000011100001110000000000
    img8 = 1000000001111111100000000000
    img9 = 1000000000111111000000000000
    output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    return output_array

def all_intro():


def swap(output_array):
    inv = 1111111111111111111111111111
    for i in range(10):

        output_array[i] = inv - output_array[i]
        #print(output_array[i])
        #time.sleep(0.5)

def set_zero():
    return [0 for _ in range(10)]

def on_press(key):
    global verti, pos1, pos2, pressed_key
    #print('{0} pressed'.format(key))

    try:
        if key.char == 'w':
            pressed_key['w'] = True

            verti = max(verti - 1, 0)

        elif key.char == 's':
            pressed_key['s'] = True

            verti = min(8, verti + 1)

        elif key.char == 'd':
            pressed_key['d'] = True

            pos1 = max(11, pos1//10)
            pos2 = max(11, pos2//10)

        elif key.char == 'a':
            pressed_key['a'] = True

            pos1 = min(1100000000000000000000000000, pos1 * 10)
            pos2 = min(1100000000000000000000000000, pos2 * 10)

    except:

        if key == Key.alt:
            pressed_key[Key.alt] = True

            verti = max(verti - 1, 0)

        elif key == Key.cmd:
            pressed_key[Key.cmd] = True

            verti = min(8, verti + 1)

        elif key == Key.alt_r:
            pressed_key[Key.alt_r] = True

            pos1 = max(11, pos1//10)
            pos2 = max(11, pos2//10)

        elif key == Key.cmd_r:
            pressed_key[Key.cmd_r] = True

            pos1 = min(1100000000000000000000000000, pos1 * 10)
            pos2 = min(1100000000000000000000000000, pos2 * 10)

        elif key == Key.shift_r:
            init()

def on_release(key):
    global pressed_key, break_loop

    try:
        if key.char in ['w','s','a','d']:
            pressed_key[key.char] = False

    except:
        if key in [Key.alt, Key.cmd,Key.alt_r, Key.cmd_r]:
            pressed_key[key] = False

        elif key == Key.shift:
            print('pressed shift')
            break_loop = True
            return False


def render(bullet_list, dead=False):
    global copy_array

    if dead:
        copy_array = [(x % 10) * 10  ** (L-1) + (x // 10) for x in copy_array]
        #if random.random() > 0.5:
        #print(copy_array)
        #swap(copy_array)

    else:
        copy_array = [x for x in output_array]
        copy_array[verti] += pos1
        copy_array[verti + 1] += pos2

        for i in range(len(bullet_list)):
            tag, val, dx, sign, pos, stack = bullet_list[i]
            if pos < 0 or pos > 9 or val > 10 ** (L-1) or val < 0:
                continue
            copy_array[int(pos)] += val
            if tag == 'h':
                stack += dx * multiplier
                pw = int(stack)
                bullet_list[i][-1] = stack - pw
                if sign > 0:
                    bullet_list[i][1] //= (10 ** pw)
                else:
                    bullet_list[i][1] *= (10 ** pw)

            else:
                if sign > 0:
                    bullet_list[i][4] += dx * multiplier
                else:
                    bullet_list[i][4] -= dx * multiplier

    for line in copy_array:
        print('{0:028d}'.format(line))

    print('press left shift to exit, press right shift to restart')

def create_bullet():
    if random.random() > 0.5:
        # Horizontal Bullet
        tag = 'h'
        dx = random.choice([1,2])
        sign = random.choice([1,-1])
        pos = random.choice(range(10))
        stack = 0
        if sign > 0:
            val = 10 ** (L-1)
        else:
            val = 1

    else:
        # Horizontal Bullet
        tag = 'v'
        dx = random.choice([0.25,0.5,0.75])
        sign = random.choice([1,-1])
        vert = random.choice(range(28))
        val = 10 ** vert
        stack = 0
        if sign > 0:
            pos = 0
        else:
            pos = 9

    return [tag, val, dx, sign, pos, stack]

def check_dead():
    # Detect number 2 in player position
    for i, player_line in enumerate([pos1, pos2]):
        counter = 0
        while player_line > 0:
            if player_line % 10 != 0:
                if (copy_array[verti + i]//(10 ** counter)) % (10) > 3:
                    return True
            counter += 1
            player_line //= 10

    return False

def init():
    global output_array, copy_array, t, pos1, pos2, \
        bullet_list, dead, array_copy, break_loop, verti
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
    pos1 = 3300000000000000
    pos2 = 3300000000000000
    verti = 4

    output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    copy_array = None

    t = 0

    bullet_list = []
    dead = False
    array_copy = False
    break_loop = False
    all_intro()

with Listener(on_press=on_press, on_release=on_release) as listener:
    init()
    while True:

        if break_loop:
            break

        if dead:
            if not array_copy:
                score = t // 10
                copy_array = die()
                array_copy = True
            if (t % 10) == 0:
                swap(copy_array)
            render(bullet_list, dead)
            print('Your Score: ', score)

        else:
            print('Score: ',t // 10)
            if t % 7 == 0:
                bullet_list.append(create_bullet())
            render(bullet_list)
            dead = check_dead()

        time.sleep(multiplier * 0.1)
        clear()
        #print ("\n" * 50)
        t += 1

    listener.join()
