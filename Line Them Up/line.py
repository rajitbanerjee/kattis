"""https://open.kattis.com/problems/lineup"""

N = int(input())
players = []
for _ in range(N):
    players.append(input())

if players == sorted(players):
    print("INCREASING")
elif players == sorted(players)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")

