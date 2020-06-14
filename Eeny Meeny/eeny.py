"""https://open.kattis.com/problems/eenymeeny"""


rhyme = len(input().split())
n = int(input())
kids = []
for _ in range(n):
    kids.append(input())

teams = [[], []]
choose, prev = 0, 0
while len(kids) > 0:
    # choose the kid at the end of the rhyme, starting from prev
    idx = (prev + rhyme - 1) % len(kids)
    prev = idx
    teams[choose].append(kids[idx])
    # remove the chosen kid from options, and switch teams
    kids.pop(idx)
    choose = int(not choose)

for team in teams:
    print(len(team))
    for kid in team:
        print(kid)
