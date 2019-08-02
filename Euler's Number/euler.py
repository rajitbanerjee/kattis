"""https://open.kattis.com/problems/eulersnumber"""

from math import factorial as fact

n = int(input())
# approximation: after n = 14, inaccuracy is insignificant 
n = 14 if n > 14 else n

euler = 0
for i in range(n + 1):
    euler += 1 / fact(i)

print(euler)