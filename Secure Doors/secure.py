"""https://open.kattis.com/problems/securedoors"""

n = int(input())
ans, side = [], []
for _ in range(n):
    (act, person) = input().split()
    if act == "entry":
        if person not in side:
            ans.append(f"{person} entered")
            side.append(person)
        else:
            ans.append(f"{person} entered (ANOMALY)")
    else:
        if person in side:
            ans.append(f"{person} exited")
            side.remove(person)
        else:
            ans.append(f"{person} exited (ANOMALY)")

for a in ans:
    print(a)