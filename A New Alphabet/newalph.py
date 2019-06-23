"""https://open.kattis.com/problems/anewalphabet"""

import string

def main():
    text = input()

    for c in text:
        if c.isalpha():
            print(new(c), end = '')
        else:
            print(c, end = '')

def new(c):
    dic = {
        'a': '@', 'b': '8', 'c': '(', 'd': '|)',
        'e': '3', 'f': '#', 'g': '6', 'h': '[-]',
        'i': '|', 'j': '_|', 'k': '|<', 'l': '1',
        'm': '[]\/[]', 'n': '[]\[]', 'o': '0', 'p': '|D',
        'q': '(,)', 'r': '|Z', 's': '$', 't': '\'][\'',
        'u': '|_|', 'v': '\/', 'w': '\/\/', 'x': '}{',
        'y': '`/', 'z': '2'
    }
    return dic[c.lower()]
           


if __name__ == '__main__':
    main()
    