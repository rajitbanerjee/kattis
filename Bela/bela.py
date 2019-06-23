"""https://open.kattis.com/problems/bela"""

def main():
    inp = input().split()
    N = int(inp[0]) # number of hands
    domi = inp[1] # dominant suit

    # dominant and non-dominant suit values in list for each dict item
    vals = {
        'A': [11, 11], 
        'K': [4, 4],
        'Q': [3, 3],
        'J': [20, 2],
        'T': [10, 10],
        '9': [14, 0],
        '8': [0, 0],
        '7': [0, 0]
    }

    total = 0
    for i in range(4 * N):
        card = input()
        if card[1] == domi:
            total += vals[card[0]][0]
        else:
            total += vals[card[0]][1]

    print(total)

if __name__ == '__main__':
    main()




