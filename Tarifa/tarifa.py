"""https://open.kattis.com/problems/tarifa"""

def main():
    X = int(input())
    N = int(input())

    used = 0
    for i in range (N):
        used += int(input())
    
    avail = X * N

    print(avail - used + X)

if __name__ == '__main__':
    main() 