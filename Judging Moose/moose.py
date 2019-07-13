"""https://open.kattis.com/problems/judgingmoose"""

l, r = map(int, input().split())
if l == r:
    if r == 0:
        print("Not a moose")
    else:
        print(f"Even {r*2}")
else:
    print(f"Odd {max(l, r)*2}")
