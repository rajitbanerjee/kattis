"""https://open.kattis.com/problems/skener"""

R, C, Zr, Zc = map(int, input().split())
matrix = []
for _ in range(R):
    row = list(input())
    matrix.append(row)

for row in matrix:
    for _ in range(Zr):
        for elem in row:
            for _ in range(Zc):
                print(elem, end = '')
        print()