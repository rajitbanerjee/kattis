"""https://open.kattis.com/problems/kafkaesque"""

k = int(input())
desks, passes = [], 0

for _ in range(k):
    desks.append(int(input()))

while len(desks) != 0:
    passes, i = passes + 1, 1
    for i in range(1, len(desks)):
        if desks[i] < desks[i - 1]:
            break
        if i == len(desks) - 1:
            i += 1
    desks = desks[i:]

print(passes)
