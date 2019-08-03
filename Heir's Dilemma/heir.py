"""https://open.kattis.com/problems/heirsdilemma"""

L, H = map(int, input().split())

def isPossible(num):
    n = num
    digits = []
    while n != 0:
        d = n % 10
        if d != 0:
            if d not in digits:
                digits.append(d)
                if num % d != 0:
                    return False
        n = n // 10

    if len(digits) == len(str(num)):
        return True

count = 0
for i in range(L, H + 1):
    if isPossible(i):
        count += 1

print(count)