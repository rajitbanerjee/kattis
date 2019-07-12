"""https://open.kattis.com/problems/railroad2"""

_, Y = map(int, input().split())
# same as Y % 2 == 1
print("impossible") if Y & 1 else print("possible")