"""https://open.kattis.com/problems/quickestimate"""

N = int(input())
ans = []

for _ in range(N):
    ans.append(len(input()))

for a in ans:
    print(a)
    
