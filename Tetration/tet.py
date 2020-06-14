"""https://open.kattis.com/problems/tetration"""

from math import log, e

N = float(input())

# a^N = N 
## => N ln a = ln N 
## => a = e^(ln N / N)
print(pow(e, log(N) / N))
