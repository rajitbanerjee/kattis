"""https://open.kattis.com/problems/avion"""

codes = []
for _ in range(5):
    codes.append(input())

found = False
for i in range(5):
    if "FBI" in codes[i]:
        print(i + 1, end=' ')
        found = True

if not found:
    print("HE GOT AWAY!")