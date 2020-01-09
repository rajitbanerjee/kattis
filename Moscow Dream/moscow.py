"""https://open.kattis.com/problems/moscowdream"""

a, b, c, n = map(int, input().split())
if 0 not in [a, b, c] and a + b + c >= n >= 3:
    print("YES")
else:
    print("NO")