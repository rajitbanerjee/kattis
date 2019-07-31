"""https://open.kattis.com/problems/relocation"""

_, Q = map(int, input().split())
pos = list(map(int, input().split()))
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # update company location
        pos[query[1] - 1] = query[2]
    else:
        # compute the distance between 2 companies
        ans.append(abs(pos[query[1] -1] - pos[query[2] -1]))

for a in ans:
    print(a)
