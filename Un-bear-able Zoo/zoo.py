"""https://open.kattis.com/problems/zoo"""

i, ans = 0, []
while True:
    n = int(input())
    if n == 0:
        break

    i += 1
    ans.append(f"List {i}:")
    animals = {}
    for _ in range(n):
        ani = input().split()[-1].lower()
        if ani not in animals:
            animals[ani] = 0
        animals[ani] += 1

    for k in sorted(animals.keys()):
        ans.append(f"{k} | {animals[k]}")

for a in ans:
    print(a)
