"""https://open.kattis.com/problems/tri"""


def checkValidEqn(a, b, c):
    sign = ''
    if a + b == c:
        sign = '+'
    elif a - b == c:
        sign = '-'
    elif a * b == c:
        sign = '*'
    elif a//b == c:
        sign = '/'
    return sign


def main():
    nums = list(map(int, input().split()))
    a, b, c = nums
    
    if checkValidEqn(a, b, c) != '':
        sign = checkValidEqn(a, b, c)
        print(f"{a}{sign}{b}={c}")

    elif checkValidEqn(b, c, a) != '':
        sign = checkValidEqn(b, c, a)
        print(f"{a}={b}{sign}{c}")


main()
