"""https://open.kattis.com/problems/cudoviste"""

R, C = map(int, input().split())
squashed = [0] * 5
mat = []

for _ in range(R):
    mat.append(list(input()))

for i in range(R - 1):
    for j in range(C - 1):
        space = [mat[i][j], mat[i][j + 1], mat[i + 1][j], mat[i + 1][j + 1]]
        buildings = space.count('#')
        cars = space.count('X')

        if buildings == 0:
            squashed[cars] += 1

for cars in squashed:
    print(cars)
