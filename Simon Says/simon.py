"""https://open.kattis.com/problems/simonsays"""

N = int(input())
ans = []
for _ in range(N):
    line = input()
    if line.startswith("Simon says"):
        ans.append(line[11:])

for a in ans:
    print(a)
