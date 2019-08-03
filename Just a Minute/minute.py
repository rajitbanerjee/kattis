"""https://open.kattis.com/problems/justaminute"""

N = int(input())
expected, actual = [], []
for _ in range(N):
    M, S = map(int, input().split())
    expected.append(M)
    actual.append(S)

sl_minute = sum(actual)/(60 * sum(expected))
if sl_minute <= 1:
    print("measurement error")
else:
    print(sl_minute)