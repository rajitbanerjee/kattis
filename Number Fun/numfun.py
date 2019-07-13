"""https://open.kattis.com/problems/numberfun"""

N = int(input())

def isPossible(a, b, c):
    if c in [a+b, abs(a-b), a*b, a/b, b/a]:
        return "Possible"
    else:
        return "Impossible"

ans = []
for _ in range(N):
    a, b, c = map(int, input().split())
    ans.append(isPossible(a, b, c))

for a in ans:
    print(a)