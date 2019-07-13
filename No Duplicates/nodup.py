"""https://open.kattis.com/problems/nodup"""

line = input().split()
freq = {}

def isRep(line, freq):
    for each in line:
        if each not in freq:
            freq[each] = 0

        freq[each] += 1
        if freq[each] > 1:
            return "no"
            
    return "yes"

print(isRep(line, freq))


            