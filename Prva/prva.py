"""https://open.kattis.com/problems/prva"""

def addWords(words=[], array=[]):
    for each in array:
        parts = each.split("#")
        # add words to list
        words.extend(parts)

    # remove elements with length < 2
    i, length = 0, len(words)
    while i < length:
        if len(words[i]) < 2:
            words.remove(words[i])	
            length -= 1
            continue
        i += 1
    
    return words

R, C = map(int, input().split())
horizontal = []
vertical = [[[] for _ in range(R)] for _ in range(C)]

for i in range(R):
    # input lines
    horizontal.append(input())
    for j in range(C):
        vertical[j][i] = horizontal[i][j]

for i, each in enumerate(vertical):
    vertical[i] = "".join(vertical[i])   

words = addWords(addWords([], horizontal), vertical)

print(sorted(words)[0])