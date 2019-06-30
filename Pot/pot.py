"""https://open.kattis.com/problems/pot"""

N = int(input())
X = 0
for _ in range(N):
    p = int(input())
    X += (p // 10) ** (p % 10)
print(X)
