"""https://open.kattis.com/problems/unlockpattern"""

matrix = [[0] * 3] * 3
points = {}

# compute the distance between two points
def dist(P, Q):
    x1, y1 = P
    x2, y2 = Q
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

for i in range(3):
    matrix[i] = list(map(int, input().split()))
    for j in range(3):
        points[matrix[i][j]] = (i, j)

total = 0
for i in range(1, 9):
    total += dist(points[i], points[i + 1])

print(total)

