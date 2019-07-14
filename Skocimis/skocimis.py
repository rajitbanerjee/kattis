"""https://open.kattis.com/problems/skocimis"""

A, B, C = map(int, input().split())
print(max(B - A, C - B) - 1)