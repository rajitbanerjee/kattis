"""https://open.kattis.com/problems/oddmanout"""

N = int(input())
ans = []

for i in range(N):
    _ = input()
    codes = input().split()
    for c in codes:
        if codes.count(c) == 1:
            ans.append(f"Case #{i+1}: {c}")
            break

for a in ans:
    print(a)