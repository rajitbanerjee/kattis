"""https://open.kattis.com/problems/tolower"""

solve = 0
P, T = map(int, input().split())

for i in range(P):
    solve += 1
    impossible = False
    for j in range(T):
        line = input()
        # check if lowercase(first letter) will not suffice
        if not impossible and line[0].lower() + line[1:] != line.lower():
            solve -= 1
            impossible = True


print(solve)
