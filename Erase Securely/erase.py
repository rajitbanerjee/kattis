"""https://open.kattis.com/problems/erase"""

import math
N = int(input())
file1, file2 = input(), input()

failed = False
if N & 1:
    for i in range(len(file1)):
        if int(file1[i]) != 1 - int(file2[i]):
            failed = True
else:
    if file1 != file2:
        failed = True
    

if failed:
    print("Deletion failed")
else:
    print("Deletion succeeded")
