"""https://open.kattis.com/problems/guess"""

import sys
lo, hi = 1, 1000 

# guess the correct number using bisection search
while lo <= hi:
    guess = (lo + hi) // 2
    print(guess)
    sys.stdout.flush()

    result = input()
    if result == "lower":
        hi = guess - 1
    elif result == "higher":
        lo = guess + 1
    else:
        exit()
