"""https://open.kattis.com/problems/sodasurpler"""

e, f, c = map(int, input().split())
empty, sodas = e + f, 0
prev = 0
while(empty >= c):  
    sodas += empty // c
    # new empty bottles + remaining empty from last time
    empty = empty // c + empty % c

print(sodas)
