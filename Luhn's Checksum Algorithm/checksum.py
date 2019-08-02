"""https://open.kattis.com/problems/luhnchecksum"""

ans = []
def checkSum(n):
    total, i = 0, 0
    for dig in n[::-1]:
        if i % 2 == 1:
            d = 2 * int(dig)
        else:
            d = int(dig)

        if d > 9:
            d = d % 10 + d // 10
        total += d
        i += 1
    
    if total % 10 == 0:
        return "PASS"
    else:
        return "FAIL"

for _ in range(int(input())):
    ans.append(checkSum(input()))

for a in ans:
    print(a)

