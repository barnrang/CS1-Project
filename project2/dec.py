'''
The following program display the repeating decimal of 1/n
where n > 1. We pre-calculate the position where the repeatition start.
Using list, set default -1, record the position for each remainder.
If a remainder was assigned already, the assigned value is where the repeat
decimal start.

We re-run the loop again but print out the '(' at the repeating-start position
if it is no repeating, then just print out normally.

'''
from time import sleep
import sys
from decimal import *

d = int(input("Input a denominator: "))
count = 0
done = False
x = 1
used = [-1 for _ in range(d+1)]
loop_st_idx = None
used[1] = 0

while not done:
    count += 1
    x *= 10
    q = x // d
    r = x % d
    if r == 0:
        done = True
    else:
        x = r
        if used[r] == -1:
            used[r] = count
        else:
            done = True
            loop_st_idx = used[r]

# Print Function
done = False
used = [-1 for _ in range(d+1)]
count = 0
x = 1
used[1] = 0

print(f'1/{d} = 0.', end='', flush=True)

while not done:
    if loop_st_idx is not None and count == loop_st_idx:
        print('(', end='', flush=True)
    count += 1
    x *= 10
    q = x // d
    r = x % d
    print(f'{q}', end='', flush=True)
    sleep(0.02)
    if r == 0:
        done = True
    else:
        x = r
        if used[r] == -1:
            used[r] = count
        else:
            done = True

if loop_st_idx is not None:
    print(')')
else:
    print('')

getcontext().prec = 50
print(f'Actual value = {(Decimal(1)/Decimal(d)).to_eng_string()}')
