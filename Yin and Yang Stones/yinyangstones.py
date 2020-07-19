"""https://open.kattis.com/problems/yinyangstones"""

from collections import Counter
if __name__ == '__main__':
    w, b = Counter(input()).values()
    print(int(w == b))
