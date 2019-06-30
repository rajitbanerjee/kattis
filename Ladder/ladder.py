"""https://open.kattis.com/problems/ladder"""

from math import sin, radians, ceil
h, v = list(map(int, input().split()))

length = ceil(h / sin(radians(v)))
print(length)
