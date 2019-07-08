"""https://open.kattis.com/problems/detaileddifferences"""

n = int(input())

def diff(a, b):
    s = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            s += "."
        else:
            s += "*"
    return s

ans = []
for _ in range(n):
    line1 = input()
    line2 = input()
    ans.extend([line1, line2, diff(line1, line2), "\n"])

for a in ans:
    print(a)


