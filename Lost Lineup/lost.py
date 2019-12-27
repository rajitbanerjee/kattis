"""https://open.kattis.com/problems/lostlineup"""

n = int(input())
d = list(map(int, input().split()))

lineup = [0] * n
lineup[0] = 1

for person, pos in zip(range(2, n + 1), d):
    lineup[pos + 1] = person

for each in lineup:
    print(each, end=' ')