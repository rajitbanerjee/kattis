"""https://open.kattis.com/problems/zamka"""

L = int(input())
D = int(input())
X = int(input())

def digitSum(n):
    s = 0
    while(n > 0):
        s += n % 10
        n = n // 10
    return s

N, M = D, L
for i in range(L, D + 1):
    if digitSum(i) == X:
        if i < N:
            N = i
        if i > M:
            M = i
    
print(N)
print(M)
