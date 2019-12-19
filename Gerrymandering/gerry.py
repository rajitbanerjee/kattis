"""https://open.kattis.com/problems/gerrymandering"""

P, D = map(int, input().split())
districts = {}

for _ in range(P):
    d, a, b = map(int, input().split())
    if d not in districts.keys():
        districts[d] = [0, 0]
    districts[d][0] += a
    districts[d][1] += b

wA, wB, V = 0, 0, 0
for i in range(1, D + 1):
    ansRow = []
    # find the winner of the election
    w = 0 if districts[i][0] > districts[i][1] else 1
    ansRow.append(chr(w + 65))

    # wasted votes of winner
    winnerWaste = districts[i][w] - sum(districts[i])//2 - 1
    # wasted votes of loser
    loserWaste = districts[i][1 - w]
    ansRow.extend([winnerWaste, loserWaste])

    if w == 1:
        ansRow[1], ansRow[2] = ansRow[2], ansRow[1]

    # display answers
    for each in ansRow:
        print(each, end=' ')
    print()

    # update total wasted votes of each party
    wA += ansRow[1]
    wB += ansRow[2]
    # update total number of voters
    V += sum(districts[i])

# compute and display efficiency gap
E = abs(wA - wB)/V
print(round(E, 10))
