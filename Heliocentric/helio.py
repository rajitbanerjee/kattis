"""https://open.kattis.com/problems/heliocentric"""

import sys

def numDays(e, m):
    days = 0
    while True:
        if (e + days) % 365 == (m + days) % 687:
            return days
        days += 1

ans = []
for line in sys.stdin:
    e, m = map(int, line.split())
    ans.append(numDays(e, m))

for i, a in enumerate(ans):
    print(f"Case {i + 1}: {a}")