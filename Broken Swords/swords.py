"""https://open.kattis.com/problems/brokenswords"""


def invert(bit: int) -> int:
    return int(not bit)


def main() -> None:
    n = int(input())
    tb, lr = 0, 0
    for _ in range(n):
        for i, c in enumerate(input()):
            if c == '0':
                if i < 2:
                    tb += 1
                else:
                    lr += 1

    swords = min(tb // 2, lr // 2)
    rem_tb, rem_lr = tb - 2 * swords, lr - 2 * swords

    print(f"{swords} {rem_tb} {rem_lr}")


main()
