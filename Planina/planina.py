"""https://open.kattis.com/problems/planina"""

def mid(n):
    if n == 0:
        return 2
    else:
        return 2 * mid(n-1) - 1
      
n = int(input())
print(mid(n)**2)


