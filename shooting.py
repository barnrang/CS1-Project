# shooting.py
# Output: Dodge the Bullet
import time
import os
import random
from pynput.keyboard import Key, Controller, Listener
clear = lambda : os.system('clear')

def die():
    img0 = 11111000011111110001111110000
    img1 = 11001100011111110001111110000
    img2 = 11000110000111000001100000000
    img3 = 11000110000111000001100000000
    img4 = 11000110000111000001111110000
    img5 = 11000110000111000001111110000
    img6 = 11000110000111000001100000000
    img7 = 11000110000111000001100000000
    img8 = 11001100011111110001111110000
    img9 = 11111000011111110001111110000
    output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
    return output_array

def set_zero():
    return [0 for _ in range(10)]


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
pos1 = 11000000000000000
pos2 = 11000000000000000
verti = 4

output_array = [img0,img1,img2,img3,img4,img5,img6,img7,img8,img9]
copy_array = None

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

def render(bullet_list, dead=False):
    global copy_array

    if dead:
        copy_array = [(x % 10) * 10  ** (L-1) + (x // 10) for x in copy_array]

    else:
        copy_array = [x for x in output_array]
        copy_array[verti] += pos1
        copy_array[verti + 1] += pos2

        for i in range(len(bullet_list)):
            tag, val, dx, sign, pos = bullet_list[i]
            if pos < 0 or pos > 9 or val > 10 ** (L-1) or val < 0:
                continue
            copy_array[pos] += val
            if tag == 'h':
                if sign > 0:
                    bullet_list[i][1] //= dx
                else:
                    bullet_list[i][1] *= dx

            else:
                if sign > 0:
                    bullet_list[i][4] += 1
                else:
                    bullet_list[i][4] -= 1

    for line in copy_array:
        print('{0:028d}'.format(line))

def create_bullet():
    if random.random() > 0.5:
        # Horizontal Bullet
        tag = 'h'
        dx = random.choice([10,100])
        sign = random.choice([1,-1])
        pos = random.choice(range(10))
        if sign > 0:
            val = 1000000000000000000000000000
        else:
            val = 1

    else:
        # Horizontal Bullet
        tag = 'v'
        dx = 10
        sign = random.choice([1,-1])
        vert = random.choice(range(28))
        val = 10 ** vert
        if sign > 0:
            pos = 0
        else:
            pos = 9

    return [tag, val, dx, sign, pos]

def check_dead():
    # Detect 2 in player position
    for i, player_line in enumerate([pos1, pos2]):
        counter = 0
        while player_line > 0:
            if player_line % 10 != 0:
                if (copy_array[verti + i]//(10 ** counter)) % (10) > 1:
                    return True
            counter += 1
            player_line //= 10


    return False

bullet_list = []
dead = False
array_copy = False
with Listener(on_press=on_press, on_release=on_release) as listener:

    while t < 1000:
        if dead:
            if not array_copy:
                copy_array = die()
                array_copy = True
            render(bullet_list, dead)

        else:
            
            if t % 5 == 0:
                bullet_list.append(create_bullet())
            render(bullet_list)
            dead = check_dead()

        time.sleep(0.1)
        clear()
        t += 1
        print(verti)



    listener.join()
