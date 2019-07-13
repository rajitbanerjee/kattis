"""https://open.kattis.com/problems/helpaphd"""

N = int(input())
ans = []
for _ in range(N):
    problem = input().split('+')
    if len(problem) == 2:
        ans.append(int(problem[0]) + int(problem[1]))
    else:
        ans.append("skipped")

for a in ans:
    print(a)