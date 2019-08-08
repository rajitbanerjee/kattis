"""https://open.kattis.com/problems/chanukah"""

def numCandles(days):
    d = int(days)
    return int(d * (0.5 * d  + 1.5))

ans = []
for _ in range(int(input())):
    ans.append(numCandles(input().split()[1]))

for i, a in enumerate(ans):
    print(i + 1, a)