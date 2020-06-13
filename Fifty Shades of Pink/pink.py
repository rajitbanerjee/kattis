"""https://open.kattis.com/problems/fiftyshades""" 

count = 0
for _ in range(int(input())):
    color = input().lower()
    if "pink" in color or "rose" in color:
        count += 1

if count == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(count)
