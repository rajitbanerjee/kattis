"""https://open.kattis.com/problems/oddities"""

n = int(input())

def odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

ans = []
for i in range(n):
    x = int(input())
    ans.append(str(x) + " is " + odd(x))

for a in ans:
    print(a)