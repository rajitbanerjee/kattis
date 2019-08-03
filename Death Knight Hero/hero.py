"""https://open.kattis.com/problems/deathknight"""

won = 0
for _ in range(int(input())):
    moves = input()
    if "CD" not in moves:
        won += 1

print(won)