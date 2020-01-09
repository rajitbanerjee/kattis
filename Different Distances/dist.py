"""https://open.kattis.com/problems/differentdistances"""

ans = []
while True:
    line = input()
    if line == '0':
        break
    else:
        x1, y1, x2, y2, p = map(float, line.split())
    ans.append(pow(pow(abs(x1 - x2), p) + \
        pow(abs(y1 - y2), p), 1/p))

for a in ans:
    print(a)