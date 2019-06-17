"""
https://open.kattis.com/problems/faktor
"""
from math import ceil
nums = list(map(int, input().split()))
A, I = nums[0], nums[1]

scientists = A
while True:
    if ceil(scientists/A) == I:
        print(scientists)
        break
    else:
        scientists += 1