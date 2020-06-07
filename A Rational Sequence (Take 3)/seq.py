"""https://open.kattis.com/problems/rationalsequence3"""


def main() -> None:
    ans = []
    P = int(input())
    for _ in range(P):
        line = list(map(int, input().split()))
        ans.append(f"{line[0]} {traverse(line[1])}")

    for a in ans:
        print(a)


def traverse(n: int) -> str:
    back_track = []
    while n != 1:
        # trace the steps from node n to 1
        back_track.append("R" if n % 2 else "L")
        n //= 2

    p, q = 1, 1
    # follow the traced steps and update p and q at each turn
    for move in back_track[::-1]:
        if move == "L":
            q = p + q
        else:
            p = p + q

    return f"{p}/{q}"


main()
