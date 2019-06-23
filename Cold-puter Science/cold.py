"""https://open.kattis.com/problems/cold"""

def main():
    n = int(input())
    temps = list(map(float, input().split()))

    count = 0
    for t in temps:
        if t < 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()