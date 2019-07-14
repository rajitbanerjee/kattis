"""https://open.kattis.com/problems/soylent"""

from math import ceil

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    ans.append(ceil(N / 400))

for a in ans:
    print(a)