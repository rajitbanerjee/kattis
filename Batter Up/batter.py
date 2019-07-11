"""https://open.kattis.com/problems/batterup"""

_ = input()
at_bats = list(map(int, input().split()))

total, n = 0, 0
for each in at_bats:
    if each != -1:
        total += each
        n += 1
print(total/n)