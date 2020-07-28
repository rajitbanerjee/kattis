"""https://open.kattis.com/problems/drunkvigenere"""

def decrypt(C: str, K: str) -> str:
    res = ""
    for i in range(len(K)):
        # Calculate shift (+/-)
        shift = pow(-1, i + 1) * pos(K[i])
        # Shift characters % 26
        res += chr((pos(C[i]) + shift) % 26 + 65)
    return res

def pos(letter) -> int:
    return ord(letter) - 65

if __name__ == '__main__':
    C, K = input(), input()
    print(decrypt(C, K))
