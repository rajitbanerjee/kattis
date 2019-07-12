"""https://open.kattis.com/problems/stararrangements"""

S = int(input())
print(str(S) + ":")

for x in range(2, S//2 + 2):
    if  S % (2 * x - 1) in [0, x]:
        print(str(x) + "," + str(x-1))
    if S % x == 0: 
        print(str(x) + "," + str(x))
    
