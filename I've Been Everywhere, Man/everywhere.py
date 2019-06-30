"""https://open.kattis.com/problems/everywhere"""

T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    memo = {}
    for _ in range(n):
        city = input()
        memo[city] = 1
    ans.append(len(memo.keys()))

for a in ans:
    print(a)

