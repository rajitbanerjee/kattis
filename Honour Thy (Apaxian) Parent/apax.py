"""https://open.kattis.com/problems/apaxianparent"""

Y, P = input().split()

if Y[-1] == 'e':
    print(Y + 'x' + P)
elif Y[-1] in ['a', 'i', 'o', 'u']:
    print(Y[:-1] + "ex" + P)
elif Y[-2:] == "ex":
    print(Y + P)
else:
    print(Y + "ex" + P)