"""https://open.kattis.com/problems/pokerhand"""

cards = input().split()
name = ['T', 'J', 'Q', 'K', 'A']
freq = [0] * 13

for each in cards:
    rank, suit = each
    if rank in name:
        freq[name.index(rank) + 8] += 1
    else:
        freq[int(rank) - 2] += 1

print(max(freq))