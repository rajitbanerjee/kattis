"""https://open.kattis.com/problems/rhyming"""

import string
S = input()

E = int(input())
endings = []
for _ in range(E):
    # input each list of rhyming word-endings
    ends = input().split()
    for each in ends:
        if S.endswith(each):
            # common word rhymes with the current list of word-endings
            endings.extend(ends)
            break

P = int(input())
phrases = []
for _ in range(P):
    # input the phrases to be checked
    phrases.append(input())

ans = []
for i, p in enumerate(phrases):
    flag = False # reset flag for each iteration
    for end in endings:
        if p.endswith(end):
            # set flag if phrase rhymes with a possible word-ending
            flag = True
            break
    if flag:
        ans.append("YES")
    else:
        ans.append("NO")

for a in ans:
    print(a)
        




