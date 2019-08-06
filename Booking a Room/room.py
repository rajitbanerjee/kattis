"""https://open.kattis.com/problems/bookingaroom"""

from random import randint

r, n = map(int, input().split())
if r == n:
    print("too late")
    exit()

booked = []
for _ in range(n):
    booked.append(int(input()))

n = randint(1, r)
while n in booked:
    # keep on shuffling until you get an empty room
    n = randint(1, r)

print(n)