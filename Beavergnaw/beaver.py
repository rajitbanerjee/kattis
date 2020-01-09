"""https://open.kattis.com/problems/beavergnaw"""

from math import pi
ans = []
while True:
    D, V = map(int, input().split())
    if D == V == 0:
        break
    else:
        # changed the subject of formula to 'd'
        # V = vol. of cylinder - (2 * vol. of frustum + vol. of small cylinder)
        ans.append(pow(pow(D, 3) - 6 * V / pi, 1/3))

for a in ans:
    print(a)