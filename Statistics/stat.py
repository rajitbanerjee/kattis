"""https://open.kattis.com/problems/statistics"""

from sys import stdin


def stat(lst: list) -> str:
    return f"{min(lst)} {max(lst)} {(max(lst) - min(lst))}"


if __name__ == '__main__':
    ans, i = [], 1
    for line in stdin.readlines():
        data = list(map(int, line.split()))[1:]
        ans.append(f"Case {i}: {stat(data)}")
        i += 1

    for a in ans:
        print(a)
