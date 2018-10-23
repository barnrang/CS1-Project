# shooting.py
# Output: Dodge the Bullet
import time
import os
import sys
import random
import platform

from recorded import recorded_input, recorded_bullet

if platform.system() == 'Windows':
    def clear(): return os.system('cls')
elif platform.system() == 'Darwin':
    def clear(): return os.system('clear')

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
multiplier = 10 / 23
restart = True

output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
copy_array = None

t = 0

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
    output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
    return output_array


def intro1():
    img0 = 1000000000001111000000000000
    img1 = 1000000000001111000000000000
    img2 = 1000000000001111000000000000
    img3 = 1000000000001111000000000000
    img4 = 1000000000001111000000000000
    img5 = 1000000000001111000000000000
    img6 = 1000000000001111000000000000
    img7 = 1000000000001111000000000000
    img8 = 1000000000001111000000000000
    img9 = 1000000000001111000000000000
    output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
    output_array = [x % (10 ** 27) for x in output_array]
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
    output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
    output_array = [x % (10 ** 27) for x in output_array]
    return output_array


def intro3():
    img0 = 1000000000011111000000000000
    img1 = 1000000000111111100000000000
    img2 = 1000000001110001110000000000
    img3 = 1000000011100000111000000000
    img4 = 1000000000000001110000000000
    img5 = 1000000000000011100000000000
    img6 = 1000000011100001110000000000
    img7 = 1000000001110000111000000000
    img8 = 1000000000111111110000000000
    img9 = 1000000000011111100000000000
    output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
    output_array = [x % (10 ** 27) for x in output_array]
    return output_array


def go():
    img0 = 1111111100000111111111100
    img1 = 11111111110000111111111100
    img2 = 111000000000000111000011100
    img3 = 110000000000000111000011100
    img4 = 110000011111000111000011100
    img5 = 110000011111000111000011100
    img6 = 110000000111000111000011100
    img7 = 111000000111000111000011100
    img8 = 11111111110000111111111100
    img9 = 1111111100000111111111100
    output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
    return output_array


def all_intro():
    clear()
    number_display = [intro3, intro2, intro1]
    for display in number_display:
        output_array = display()
        t = 0
        while t < 7:
            for line in output_array:
                print('{0:028d}'.format(line))
            time.sleep(0.1)
            if t > 1:
                output_array = midblast(output_array)
            clear()
            t += 1

    t = 0
    while t < 5:
        if t % 2 == 0:
            output_array = go()
        else:
            output_array = set_zero()
        for line in output_array:
            print('{0:028d}'.format(line))
        time.sleep(0.25)
        clear()
        t += 1


def midblast(output_array):
    copy_array = [None for _ in range(10)]
    half_width = L // 2
    for i in range(10):
        first_half = output_array[i] // (10 ** half_width)
        second_half = output_array[i] % (10 ** half_width)
        if i < 5:
            if i != 0:
                copy_array[i - 1] = (first_half * 10 ** (half_width + 2) +
                                     second_half // 100) % (10 ** L)

        else:
            if i != 9:
                copy_array[i + 1] = (first_half * 10 ** (half_width + 2) +
                                     second_half // 100) % (10 ** L)

    copy_array[4] = 0
    copy_array[5] = 0
    return copy_array


def swap(output_array):
    inv = 1111111111111111111111111111
    for i in range(10):
        output_array[i] = inv - output_array[i]


def set_zero():
    return [0 for _ in range(10)]


def source_input(key):
    global verti, pos1, pos2, pressed_key, restart

    if key == 'w':

        verti = max(verti - 1, 0)

    elif key == 's':

        verti = min(8, verti + 1)

    elif key == 'd':

        pos1 = max(11, pos1 // 10)
        pos2 = max(11, pos2 // 10)

    elif key == 'a':

        pos1 = min(1100000000000000000000000000, pos1 * 10)
        pos2 = min(1100000000000000000000000000, pos2 * 10)

def render(bullet_list, dead=False):
    global copy_array

    if dead:
        copy_array = [(x % 10) * 10 ** (L - 1) + (x // 10) for x in copy_array]

    else:
        copy_array = [x for x in output_array]
        copy_array[verti] += pos1
        copy_array[verti + 1] += pos2

        for i in range(len(bullet_list)):
            tag, val, dx, sign, pos, stack = bullet_list[i]
            if pos < 0 or pos > 9 or val > 10 ** (L - 1) or val < 0:
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
        dx = random.choice([1, 2])
        sign = random.choice([1, -1])
        pos = random.choice(range(10))
        stack = 0
        if sign > 0:
            val = 10 ** (L - 1)
        else:
            val = 1

    else:
        # Horizontal Bullet
        tag = 'v'
        dx = random.choice([0.25, 0.5, 0.75])
        sign = random.choice([1, -1])
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
                if (copy_array[verti + i] // (10 ** counter)) % (10) > 3:
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

    output_array = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9]
    copy_array = None

    t = 0

    bullet_list = []
    dead = False
    array_copy = False
    break_loop = False
    all_intro()

if __name__ == "__main__":
    after_dead_count = 0
    while True:

        if break_loop:
            break

        if restart:
            init()
            restart = False

        if dead:
            after_dead_count += 1
            if not array_copy:
                score = t // 10
                copy_array = die()
                array_copy = True
            if after_dead_count > 60:
                break
            if (t % 10) == 0:
                swap(copy_array)
            render(bullet_list, dead)
            print('Your Score: ', score)

        else:
            source_input(recorded_input[t])
            print('Score: ', t // 10)
            if t % 7 == 0:
                bullet_list.append(recorded_bullet.pop(0))
            render(bullet_list)
            dead = check_dead()

        time.sleep(multiplier * 0.1)
        clear()
        #print ("\n" * 50)
        t += 1
