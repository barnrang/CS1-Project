# moving-smile.py
# Output: Moving smiley
import time

img0 = 1000000000000000000000000000
img1 = 1000000000110000110000000000
img2 = 1000000000110000110000000000
img3 = 1000000000000000000000000000
img4 = 1000001100000000000011000000
img5 = 1000000110000000000110000000
img6 = 1000000011000000001100000000
img7 = 1000000000111111110000000000
img8 = 1000000000000000000000000000
img9 = 1000000000000000000000000000

t = 0
while t < 29:
    print(img0)
    print(img1)
    print(img2)
    print(img3)
    print(img4)
    print(img5)
    print(img6)
    print(img7)
    print(img8)
    print(img9)
    print()
    img0 = img0 // 10
    img1 = img1 // 10
    img2 = img2 // 10
    img3 = img3 // 10
    img4 = img4 // 10
    img5 = img5 // 10
    img6 = img6 // 10
    img7 = img7 // 10
    img8 = img8 // 10
    img9 = img9 // 10
    time.sleep(1/23)
    t += 1
