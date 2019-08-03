"""https://open.kattis.com/problems/falsesecurity"""

import sys

code = {
    "A": ".-",   "H": "....", "O": "---",  "V": "...-",
    "B": "-...", "I": "..",   "P": ".--.", "W": ".--",
    "C": "-.-.", "J": ".---", "Q": "--.-", "X": "-..-",
    "D": "-..",  "K": "-.-",  "R": ".-.",  "Y": "-.--",
    "E": ".",    "L": ".-..", "S": "...",  "Z": "--..",
    "F": "..-.", "M": "--",   "T": "-",
    "G": "--.",  "N": "-.",   "U": "..-",

    "_": "..--", ".": "---.",
    ",": ".-.-", "?": "----"
}

recode = {}
for k, v in code.items():
    recode[v] = k

def main():

    ans = []
    for line in sys.stdin:
        message = line[:-1]
        ans.append(decode(message))

    for a in ans:
        print(a)

def decode(message):
    morse, decoded, nums = "", "", ""
    for ch in message:
        morse += code[ch]
        nums += str(len(code[ch]))
    
    for n in nums[::-1]:
        decoded += recode[morse[:int(n)]]
        morse = morse[int(n):]
    
    return decoded

if __name__ == "__main__":
    main()