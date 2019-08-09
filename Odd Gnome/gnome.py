"""https://open.kattis.com/problems/oddgnome"""

def kingPosition(gnomes):
    for i in range(1, len(gnomes)):
        if gnomes[i] != gnomes[i - 1] + 1:
            return i + 1

ans = []
for _ in range(int(input())):
    gnomes = list(map(int, input().split()))[1:]
    ans.append(kingPosition(gnomes))

for a in ans:
    print(a)
