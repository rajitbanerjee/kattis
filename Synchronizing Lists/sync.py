"""https://open.kattis.com/problems/synchronizinglists"""

from collections import OrderedDict
ans = []
while True:
    n = int(input())
    if n == 0:
        break
    order = OrderedDict()
    A, B = [], []
    for _ in range(n):
        num = int(input())
        A.append(num)
        order[num] = 0 # initialise ordered dict

    for _ in range(n):
        num = int(input())
        B.append(num)

    A.sort()
    B.sort()
    for i in range(n):
        # synchronize the order of the lists A and B
        order[A[i]] = B[i]
    
    for each in order.values():
        ans.append(each)
    ans.append("\n")

for a in ans:
    print(a)

    
