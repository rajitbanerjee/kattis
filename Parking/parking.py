"""https://open.kattis.com/problems/parking"""

A, B, C = list(map(int, input().split()))
arr, dep = [], []
for _ in range(3):
    data = list(map(int, input().split()))
    arr.append(data[0])
    dep.append(data[1])

cost, trucks = 0, 0
for i in range(min(arr), max(dep) + 1):
    trucks += arr.count(i) - dep.count(i)
    if trucks > 0:
        cost += [A, 2 * B, 3 * C][trucks - 1]

print(cost)
