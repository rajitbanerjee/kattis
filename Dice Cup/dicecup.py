"""https://open.kattis.com/problems/dicecup"""

def main():
    N, M = list(map(int, input().split()))

    sums = {}
    # initialise dictionary
    for i in range(1, N+1):
        for j in range(1, M+1):
            sums[i+j] = 0

    # updating the count of each possible sum with the given dice
    for i in range(1, N+1):
        for j in range(1, M+1):
            sums[i+j] += 1


    for key, val in sums.items():
        if val == max(sums.values()):
            print(key)


if __name__ == '__main__':
    main()
