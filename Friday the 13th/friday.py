"""https://open.kattis.com/problems/friday"""

ans = []
def count13(D, M, days):
    count, d = 0, 0
    for i in range(len(days)):
        for j in range(days[i]):
            if d == 5 and j == 12:
                count += 1
            d = (d + 1) % 7
    return count

n = int(input())
for _ in range(n):
    D, M = map(int, input().split())
    days = list(map(int, input().split()))
    ans.append(count13(D, M, days))

for a in ans:
    print(a)
