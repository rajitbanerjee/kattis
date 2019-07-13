"""https://open.kattis.com/problems/icpcawards"""

from collections import OrderedDict

N = int(input())
rank = OrderedDict()
prizes = 12

for _ in range(N):
    uni, team = input().split()
    if uni not in rank and prizes != 0:
        rank[uni] = team
        prizes -= 1

for uni, team in rank.items():
    print(uni, team)
