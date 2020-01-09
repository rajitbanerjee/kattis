"""https://open.kattis.com/problems/thisaintyourgrandpascheckerboard"""


def transpose(matrix):
    # initialise empty matrix
    new_mat = ["" for _ in range(len(matrix[0]))]

    # transpose matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_mat[i] += list(matrix)[j][i]
    return new_mat


def checkSquareCount(matrix):
    for row in matrix:
        if row.count('B') != row.count('W'):
            return 0
    return 1


def checkConsec(matrix):
    for row in matrix:
        if 'BBB' in row or 'WWW' in row:
            return 0
    return 1


def main():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(input())

    trans = transpose(board)
    print(checkSquareCount(board) * checkConsec(board) * \
        checkSquareCount(trans) * checkConsec(trans))


main()
