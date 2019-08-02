"""https://open.kattis.com/problems/prsteni"""

def findGCD(a, b):
    if b == 0:
        return a
    else:
        return findGCD(b, a % b)

_ = input()
radii = list(map(int, input().split()))
fractions = []

numerator = radii[0]
for i in range(1, len(radii)):
    gcd = findGCD(numerator, radii[i])
    fractions.append(str(numerator//gcd) + "/" + str(radii[i]//gcd))

for f in fractions:
    print(f)
