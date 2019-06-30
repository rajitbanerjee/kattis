"""https://open.kattis.com/problems/faktor"""

from math import ceil
A, I = list(map(int, input().split()))

scientists = A
while True:
    if ceil(scientists/A) == I:
        print(scientists)
        break
    else:
        scientists += 1