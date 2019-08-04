"""https://open.kattis.com/problems/estimatingtheareaofacircle"""

import math

ans = []
while True:
    r, m, c = map(float, input().split())
    if (r, m, c) == (0, 0, 0):
        break

    area = math.pi * r * r
    estimate = c/m * ((2 * r) ** 2)
    ans.append(f"{area} {estimate}")

for a in ans:
    print(a)