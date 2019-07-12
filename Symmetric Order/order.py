"""https://open.kattis.com/problems/symmetricorder"""

ans, set_no = [], 0
while(True):
    n = int(input())
    if n == 0:
        break
    set_no += 1
    ans.append("SET " + str(set_no))

    top, bottom = [], []
    for i in range(n):
        if i % 2 == 0:
            top.append(input())
        else:
            bottom.append(input())

    for each in top:
        ans.append(each)
    for each in bottom[::-1]:
        ans.append(each)

for a in ans:
    print(a)