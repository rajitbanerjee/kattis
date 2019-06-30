"""https://open.kattis.com/problems/sevenwonders"""

cards = input()
freq = {'T':0, 'C':0, 'G':0}
for i in cards:
    freq[i] += 1

points = 0
for f in freq.values():
    points += f**2
points += min(freq.values()) * 7

print(points)