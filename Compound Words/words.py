"""https://open.kattis.com/problems/compoundwords"""

import sys

words, compounds = [], []
for line in sys.stdin:
    words.extend(line.split())

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        c1 = words[i] + words[j]
        c2 = words[j] + words[i]
        
        if c1 not in compounds:
            compounds.append(c1)
        if c2 not in compounds:
            compounds.append(c2)

print("\n".join(sorted(compounds)))