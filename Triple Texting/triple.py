"""https://open.kattis.com/problems/tripletexting"""

t = input()
size = len(t) // 3
words = [t[:size], t[size: 2*size], t[2*size: 3*size]]

# the correct word will always be in the middle of the three (when sorted)
print(sorted(words)[1])
