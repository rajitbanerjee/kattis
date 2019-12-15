"""https://open.kattis.com/problems/pieceofcake2"""

n, h, v = map(int, input().split())
volume = max(h, n - h) * max(v, n - v) * 4

print(volume)