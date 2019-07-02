"""https://open.kattis.com/problems/heartrate"""

n = int(input())

def heart(b, p):
    r = b / p 
    maxi = (b + 1) / p
    mini = (b - 1) / p
    return "{:.4f} {:.4f} {:.4f}".format(60*mini, 60*r, 60*maxi)

ans = []
for _ in range(n):
    b, p = list(map(float, input().split()))
    ans.append(heart(b, p))

for a in ans:
    print(a)