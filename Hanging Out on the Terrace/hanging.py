"""https://open.kattis.com/problems/hangingout"""

L, x = list(map(int, input().split()))
deny, total = 0, 0
for _ in range(x):
    move = input().split()
    if move[0] == "enter":
        if total + int(move[1]) > L:
            deny += 1
        else:
            total += int(move[1])
    elif move[0] == "leave":
        total -= int(move[1])

print(deny)

    




