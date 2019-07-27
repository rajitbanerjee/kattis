"""https://open.kattis.com/problems/sok"""

A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

ratios = [A/I, B/J, C/K]
mult = min(ratios)

ans = [A - mult * I, B - mult * J, C - mult * K]
for a in ans:
    print(a, end=' ')
