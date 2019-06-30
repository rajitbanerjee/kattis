"""https://open.kattis.com/problems/trik"""

moves = input()
cup = [1, 0, 0]
for move in moves:
    if move == 'A':
        cup[0], cup[1] = cup[1], cup[0]
    elif move == 'B':
        cup[1], cup[2] = cup[2], cup[1]
    else:
        cup[0], cup[2] = cup[2], cup[0]
print(cup.index(1) + 1)