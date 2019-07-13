"""https://open.kattis.com/problems/mixedfractions"""

ans = []
while(True):
    num, denom = map(int, input().split())
    if num == 0 and denom == 0:
        break
    q, r = str(num // denom), str(num % denom)
    ans.append(q + " " + r + " / " + str(denom))

for a in ans:
    print(a)