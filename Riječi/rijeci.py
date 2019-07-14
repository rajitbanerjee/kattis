"""https://open.kattis.com/problems/rijeci"""

K = int(input())
countA, countB = 1, 0

for _ in range(K):
    A, B = countA, countB # copies
    countA += countB - A # update no. of A's
    countB += A # update no. of B's

print(countA, countB)
