"""https://open.kattis.com/problems/goatrope"""

x, y, x1, y1, x2, y2 = list(map(int, input().split()))
minDist = 0

# return the distance two points (x, y) and (a, b)
def dist(x, y, a, b):
    return ((x - a)**2 + (y - b)**2)**0.5

if x not in range(x1, x2+1) and y in range(y1, y2+1):
    minDist = min(abs(x1 - x), abs(x2 - x))
elif x in range(x1, x2+1) and y not in range(y1, y2+1):
    minDist = min(abs(y1 - y), abs(y2 - y))
else:
    minDist = min(dist(x, y, x1, y1), dist(x, y, x1, y2), dist(x, y, x2, y2),
                    dist(x, y, x2, y1))

print (minDist)


