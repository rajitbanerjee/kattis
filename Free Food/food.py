"""https://open.kattis.com/problems/freefood"""

N = int(input())
days = []
for _ in range(N):
    s, t = map(int, input().split())
    for each in range(s, t+1):
        if each not in days:
            days.append(each)
print(len(days))
