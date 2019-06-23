"""https://open.kattis.com/problems/acm"""

import string

def findTime(log):
    time, solved = 0, 0
    for letter, data in log.items():
        if len(data) > 0:
            if 'right' in data:
                # time for 'right' submission is 2nd last element
                time += int(data[len(data) - 2])
                time += 20 * data.count('wrong')
                solved += 1
    print(solved, time)


def main():
    # initialise log dictionary with empty lists for all keys
    log = {}

    for let in string.ascii_uppercase:
        log[let] = list()

    while True:
        line = input().split()
        if line[0] == '-1':
            break
        log[line[1]].append(line[0])
        log[line[1]].append(line[2])
    
    findTime(log)

if __name__ == '__main__':
    main()
