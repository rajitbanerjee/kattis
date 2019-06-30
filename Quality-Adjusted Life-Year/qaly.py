"""https://open.kattis.com/problems/qaly"""

N = int(input())
total = 0
for _ in range(N):
    q, y = list(map(float, input().split()))
    total += q * y
print(round(total, 3))

