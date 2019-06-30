"""https://open.kattis.com/problems/pet"""

sums = []
for i in range(5):
    enter = list(map(int, input().split()))
    sums.append(sum(enter))

winPoints = max(sums)
winner = sums.index(winPoints) + 1
print(winner, winPoints)