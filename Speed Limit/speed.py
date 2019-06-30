"""https://open.kattis.com/problems/speedlimit"""

def findMiles(speed, time):
    total = 0
    for i in range(len(time) - 1, 0, -1):
        time[i] -= time[i-1]
    for i in range(len(speed)):
        total += speed[i] * time[i]
    return total

dist = []
while True:
    speed, time = [], []
    n = int(input())
    if n == -1:
        break
    for _ in range(n):
        data = input().split()
        speed.append(int(data[0]))
        time.append(int(data[1]))
    dist.append(findMiles(speed, time))

for miles in dist:
    print(miles, "miles")

    