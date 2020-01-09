"""https://open.kattis.com/problems/basketballoneonone"""

record = input()
score = {'A': 0, 'B': 0}
for i, ch in enumerate(record):
    if ch in ['A', 'B']:
        score[ch] += int(record[i + 1])

print('A') if score['A'] > score['B'] else print('B') 

