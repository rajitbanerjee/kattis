"""https://open.kattis.com/problems/romans"""

X = float(input())

def toRoman(X):
    return round(X * 1000 * 5280 / 4854)

print(toRoman(X))