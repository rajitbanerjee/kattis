"""https://open.kattis.com/problems/nastyhacks"""

n = int(input())
ans = []
for _ in range(n):
    r, e, c = list(map(int, input().split()))
    if r < e - c:
        ans.append("advertise")
    elif r > e - c:
        ans.append("do not advertise")
    else:
        ans.append("does not matter")

for a in ans:
    print(a)
