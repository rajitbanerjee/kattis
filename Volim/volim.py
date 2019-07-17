"""https://open.kattis.com/problems/volim"""

K, N = int(input()), int(input())
time_type, time = [], 210

for _ in range(N):
    time_type.append(tuple(input().split()))

for each in time_type:
    t, ans = int(each[0]), each[1]
    time -= t # time passes

    if time <= 0:
        # time's up, box explodes
        print(K)
        break

    if ans == 'T':
        # box passed to player on the left
        K = (K + 1) % 8
        K = 8 if K == 0 else K
        



