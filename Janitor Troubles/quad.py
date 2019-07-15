"""https://open.kattis.com/problems/janitortroubles"""

a, b, c, d = map(int, input().split())

s = (a + b + c + d) / 2 # semi perimeter

# Brahmagupta's formula
max_area = ((s - a) * (s - b) * (s - c) * (s - d)) ** 0.5
print(max_area)