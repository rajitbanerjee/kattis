"""https://open.kattis.com/problems/lastfactorialdigit"""

T = int(input())
ans = []

def factDig(n):
    f = 1
    for i in range(1, n+1):
        f = (f * (i % 10)) % 10
    return f

for _ in range(T):
    ans.append(factDig(int(input())))

for a in ans:
    print(a)