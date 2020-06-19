"""https://open.kattis.com/problems/sjecista"""

n = int(input())
# number of intersections between pairs of diagonals
print((n - 3) * (n - 2) * (n - 1) * (n) // 24)
