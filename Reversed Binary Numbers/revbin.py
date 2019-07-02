"""https://open.kattis.com/problems/reversebinary"""

# function to convert binary to decimal number
def binToDec(num: str):
    ans = 0
    for i in range(len(num)):
        ans += int(num[i]) * (2**(len(num) - i - 1))
    return ans

N = int(input())
#converting to binary, then reverse, then convert back  to decimal
print(binToDec(bin(N)[::-1][:-2]))
