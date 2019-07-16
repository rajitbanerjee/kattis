"""https://open.kattis.com/problems/drmmessages"""

import string

def main():
    encrypted = input()
    size = len(encrypted)
    half1 = rotate(encrypted[:size//2])
    half2 = rotate(encrypted[size//2:])
    merge(half1, half2)


def rotate(half):
    caps = string.ascii_uppercase
    # rotation value
    val = sum([caps.index(i) for i in half])

    rotated = ""
    for ch in half:
        rotated += caps[(caps.index(ch) + val) % 26]
    return rotated


def merge(half1, half2):
    caps = string.ascii_uppercase
    decrypted = ""
    for ch1, ch2 in zip(half1, half2):
        decrypted += caps[(caps.index(ch1) + caps.index(ch2)) % 26]
    print(decrypted)


if __name__ == '__main__':
    main()
