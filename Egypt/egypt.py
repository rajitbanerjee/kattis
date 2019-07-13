"""https://open.kattis.com/problems/egypt"""

def isRight(n):
    n.sort()
    if n[0]**2 + n[1]**2 == n[2]**2:
        return "right"
    else:
        return "wrong"

ans = []
while(True):
    line = list(map(int, input().split()))
    if line.count(0) == 3:
        break
    ans.append(isRight(line))

for a in ans:
    print(a)