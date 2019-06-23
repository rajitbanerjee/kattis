"""https://open.kattis.com/problems/3dprinter"""

from math import pow

def days(n: int) -> int:
    p = 0 # power of 2
    count = 1 # minimum number of days required
    while pow(2, p) < n:
        p += 1
        count += 1
    return count

def main():
    n = int(input()) # number of statues required
    print(days(n))

if __name__ == '__main__':
    main()