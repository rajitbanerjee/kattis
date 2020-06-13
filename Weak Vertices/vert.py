"""https://open.kattis.com/problems/weakvertices"""


def weak(mat: list) -> str:
    ans = []
    n = len(mat)
    for i in range(n):
        # there are less than 2 connected vertices or,
        # the connected vertices do not form a triangle
        if mat[i].count(1) < 2 or noTriangle(mat[i], mat):
            ans.append(i)
    return " ".join([str(i) for i in sorted(ans)])


def noTriangle(row: list, mat: list) -> bool:
    edge_indices = []
    for i, each in enumerate(row):
        if each == 1:
            edge_indices.append(i)

    # check that at least 2 vertices are connected to each other
    for i in edge_indices:
        for j in edge_indices:
            if mat[i][j] == 1:
                return False
    return True


if __name__ == '__main__':
    ans = []
    while True:
        n = int(input())
        if n == -1:
            break
        mat = []
        for _ in range(n):
            mat.append(list(map(int, input().split())))

        if n < 3:
            # too few vertices to form a triangle
            vert = [str(i) for i in range(n)]
            ans.append(" ".join(vert))
        else:
            ans.append(weak(mat))

    for a in ans:
        print(a)
