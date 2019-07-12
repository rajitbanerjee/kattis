"""https://open.kattis.com/problems/cups"""

N = int(input())

cups, radii = {}, []
for _ in range(N):
    C, R = input().split()
    if C.isdigit():
        C, R = R, int(C) // 2
    cups[int(R)] = C
    radii.append(int(R))

for each in sorted(radii):
    print(cups[each])

