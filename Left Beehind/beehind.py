"""https://open.kattis.com/problems/leftbeehind"""

ans = []
while True:
    x, y = map(int, input().split())
    if (x, y) == (0, 0):
        break
    if x + y == 13:
        ans.append("Never speak again.")
    elif x > y:
        ans.append("To the convention.")
    elif x < y:
        ans.append("Left beehind.")
    else:
        ans.append("Undecided.")

for a in ans:
    print(a)