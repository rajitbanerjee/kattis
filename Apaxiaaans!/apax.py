"""https://open.kattis.com/problems/apaxiaaans"""

name = list(input())

for i in range(len(name) - 1):
    ch = name[i]
    ch2 = name[i + 1]
    if ch != ch2:
        print(ch, end='')

print(name[-1], end='')