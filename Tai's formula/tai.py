"""https://open.kattis.com/problems/taisformula"""


def sumAreas(p1, p2):
    t1, v1 = p1
    t2, v2 = p2
    return 0.5 * (v1 + v2) * (t2 - t1)


def main():
    data = []
    for _ in range(int(input())):
        data.append(tuple(map(float, input().split())))

    area = 0
    for i in range(len(data) - 1):
        area += sumAreas(data[i], data[i + 1])
    print(area/1000)

main()
