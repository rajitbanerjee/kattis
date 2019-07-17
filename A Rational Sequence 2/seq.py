"""https://open.kattis.com/problems/rationalsequence2"""

P = int(input())
ans = []

def nodeNum(p, q):
    moves = []
    while p != q:
        if p > q:
            # current node is a right child
            p -= q
            moves.append("right")
        else:
            # current node is a left child
            q -= p
            moves.append("left")

    nodes = 1  # there is only 1 root node initially
    for m in moves[::-1]:
        # moves are reversed since new traversal starts from root, not p/q
        nodes *= 2  # each node has 2 children
        if m == "right":
            nodes += 1

    return nodes


for i in range(1, P + 1):
    line = input().split()
    num, denom = map(int, line[1].split("/"))
    ans.append(f"{i} {nodeNum(num, denom)}")

for a in ans:
    print(a)
