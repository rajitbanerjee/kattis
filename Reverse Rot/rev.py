"""https://open.kattis.com/problems/reverserot"""

import string

def encode(S, N):
    chars = string.ascii_uppercase + "_."
    new_str = ""
    for ch in S:
        ch_index = chars.index(ch)
        new_str += chars[(ch_index + N) % 28] 
    return new_str

ans = []
while(True):
    line = input().split()
    if line[0] == '0':
        break
    N, S = int(line[0]), line[1]
    ans.append(encode(S[::-1], N))

for a in ans:
    print(a)