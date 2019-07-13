"""https://open.kattis.com/problems/easiest"""

def sumDig(n):
    s = 0
    for dig in str(n):
        s += int(dig)
    return s 

ans = []
while(True):
    N = int(input())
    if N == 0:
        break
    p = 11
    while(True):
        if sumDig(N * p) == sumDig(N):
            ans.append(p)
            break
        p += 1

for a in ans:
    print(a)
        
    