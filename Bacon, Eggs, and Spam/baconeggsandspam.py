"""https://open.kattis.com/problems/baconeggsandspam"""


def solveDay(orders: dict) -> str:
    ans = []
    for k in sorted(orders.keys()):
        res = str(k) + " "
        res += " ".join(sorted(orders[k]))
        ans.append(res)
    return "\n" + "\n".join(ans) + "\n"


if __name__ == '__main__':
    ans = ""
    while True:
        n = int(input())
        if n == 0:
            break
        orders = {}
        for _ in range(n):
            line = input().split()
            for order in line[1:]:
                if order not in orders:
                    orders[order] = []
                orders[order].append(line[0])
        ans += solveDay(orders)
    print(ans)
