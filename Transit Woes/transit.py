"""https://open.kattis.com/problems/transitwoes"""


def getWaitTime(interval: int, time: int) -> int:
    arrival = interval
    while(arrival < time):
        arrival += interval
    return arrival - time


def main() -> None:
    s, t, n = map(int, input().split())
    d = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    time = s
    for i in range(n):
        time += d[i]
        time += b[i] + getWaitTime(c[i], time)

    print("yes" if (time + d[-1]) <= t else "no")


main()
