"""https://open.kattis.com/problems/sumsquareddigits"""

P = int(input())

def ssd(b, n):
    total = 0
    while n > 0:
        total += (n % b)**2
        n = n // b
    return str(total)

ans = []
for _ in range(P):
    i, b, n = map(int, input().split())
    ans.append(str(i) + " " + ssd(b, n))

for a in ans:
    print(a)