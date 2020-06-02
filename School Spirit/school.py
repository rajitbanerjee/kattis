"""https://open.kattis.com/problems/schoolspirit"""

def score(s: list) -> int:
    total = 0
    for i in range(len(s)):
        total += s[i] * (4 / 5)**i
    return total / 5

def main() -> None:
    n = int(input())
    s = []
    g = []

    for _ in range(n):
        s.append(int(input()))
    
    for i in range(n):
        copy = s.copy()
        # student with score s_i leaves
        copy.pop(i)
        # new group score
        g.append(score(copy))
    
    print(score(s)) # original group score
    print(sum(g) / n) # average new group score


main()

