"""https://open.kattis.com/problems/harshadnumbers"""

def main():
    n = int(input())

    found = False
    while not found:
        if harsh(n):
            print(n)
            found = True
            break
        else:
            n += 1

def harsh(num):
    return num % sod(num) == 0

def sod(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == '__main__':
    main() 