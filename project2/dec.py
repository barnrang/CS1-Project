from time import sleep
d = int(input("Input a denominator: "))
count = 0
done = False
x = 1
used = [0 for _ in range(d+1)]
used[1] = 1

while not done:
    count += 1
    x *= 10
    q = x // d
    r = x % d
    print(f'{count}:{q}({r})')
    sleep(0.5)
    if r == 0:
        done = True
    else:
        if used[r] == 0:
            used[r] = 1
        else:
            done = True
