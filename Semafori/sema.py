"""https://open.kattis.com/problems/semafori"""


N, L = map(int, input().split())
time, covered = 0, 0
for _ in range(N):
    D, R, G = map(int, input().split())
    time += D - covered
    covered = D
    if time % (R + G) < R:
        time += R - time % (R + G)

print(time + L - covered)
