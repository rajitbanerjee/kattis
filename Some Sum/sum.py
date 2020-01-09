"""https://open.kattis.com/problems/somesum"""

N = int(input())
if N % 2 == 1:
    print("Either")
elif N % 2 == 0 and N % 4 == 0:
    print("Even")
else:
    print ("Odd")