"""https://open.kattis.com/problems/parking2"""

from math import ceil

t = int(input())
ans = []
for _ in range(t):
    _ = input()
    pos = list(map(int, input().split()))
    avg = ceil(sum(pos)/len(pos))
    ans.append((abs(avg - min(pos)) + abs(avg - max(pos))) * 2)

for a in ans:
    print(a)