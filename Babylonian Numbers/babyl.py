"""https://open.kattis.com/problems/babylonian"""

def babylToDec(num: str):
    ans = 0
    for i in range(len(num)):
        if num[i] != '':
            ans += int(num[i]) * (60**(len(num) - i - 1))
    return ans

N = int(input())
ans = []

for _ in range(N):
    num = input().split(',')
    ans.append(babylToDec(num))

for a in ans:
    print(a)
