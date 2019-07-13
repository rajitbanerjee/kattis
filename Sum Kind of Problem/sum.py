"""https://open.kattis.com/problems/sumkindofproblem"""

P = int(input())

def sums(N):
    tot, odd, even = N * (N + 1)//2, N ** 2, N * (N + 1)
    return (tot, odd, even)

ans = []
for i in range(1, P + 1):
    _, N = map(int, input().split())
    tot, odd, even = sums(N)
    ans.append(f"{i} {tot} {odd} {even}")

for a in ans:
    print(a)
