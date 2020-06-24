"""https://open.kattis.com/problems/veci"""

from itertools import permutations

x = input()
perm = sorted(["".join(i) for i in set(permutations(x))])

if perm[-1] == x:
    print(0)
else:
    print(perm[perm.index(x) + 1])
