"""https://open.kattis.com/problems/pauleigon"""

N, P, Q = map(int, input().split())

if ((P + Q) // N) % 2 == 0:
    print("paul")
else:
    print("opponent")
