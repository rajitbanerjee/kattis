"""https://open.kattis.com/problems/grassseed"""

C, L = float(input()), int(input())
cost = 0
for _ in range(L):
    w, l = map(float, input().split())
    cost += w * l * C

print(cost)
