"""https://open.kattis.com/problems/deathstar"""

from random import randint

N = int(input())
ans = [0] * N
for i in range(N):
    row = list(map(int, input().split()))
    for num in row:
        ans[i] |= num

for a in ans:
    print(a, end = ' ')


