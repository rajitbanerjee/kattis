"""https://open.kattis.com/problems/boatparts"""

P, N = map(int, input().split())

parts, unique = [], []
for _ in range(N):
    parts.append(input())

if len(set(parts)) != P:
    print("paradox avoided")
    exit()

for i, part in enumerate(parts):
    if part not in unique:
        unique.append(part)
    if len(unique) == P:
        print(i + 1)
        exit()

print("paradox avoided")
