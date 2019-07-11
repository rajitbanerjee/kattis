"""https://open.kattis.com/problems/zanzibar"""

T = int(input())

def lowBound(seq):
    turtles = 0
    for i in range(len(seq) - 1):
        if seq[i+1] > 2 * seq[i]:
            turtles += seq[i+1] - 2 * seq[i]
    return turtles


ans = []
for _ in range(T):
    # discard the 0 at the end of the list
    seq = list(map(int, input().split()))[:-1]
    ans.append(lowBound(seq))

for a in ans:
    print(a)

