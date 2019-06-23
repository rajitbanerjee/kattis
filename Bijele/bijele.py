"""https://open.kattis.com/problems/bijele"""

def main():
    required = [1, 1, 2, 2, 2, 8]
    have = list(map(int, input().split()))

    for i in range(len(have)):
        print((required[i] - have[i]), end = ' ')

if __name__ == '__main__':
    main()
    