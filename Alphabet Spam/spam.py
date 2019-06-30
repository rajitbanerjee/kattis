"""https://open.kattis.com/problems/alphabetspam"""

import string

s = input()
white, low, upp, sym = 0, 0, 0, 0
for ch in s:
    if ch == '_':
        white += 1
    elif ch in string.ascii_lowercase:
        low += 1
    elif ch in string.ascii_uppercase:
        upp += 1
    else:
        sym += 1

tot = len(s)
print(white/tot, low/tot, upp/tot, sym/tot, sep = '\n')
