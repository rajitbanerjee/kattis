"""https://open.kattis.com/problems/chopin"""

from sys import stdin


def alt(key: str) -> str:
    dict = {
        "A#": "Bb",
        "C#": "Db",
        "D#": "Eb",
        "F#": "Gb",
        "G#": "Ab"
    }

    for k, v in dict.items():
        if k == key:
            return v
        elif v == key:
            return k

    return "UNIQUE"


def main() -> None:
    ans, i = [], 1
    for line in stdin.readlines():
        key, tonality = line.split()

        alternate = alt(key)
        if alternate == "UNIQUE":
            ans.append(f"Case {i}: {alternate}")
        else:
            ans.append(f"Case {i}: {alternate} {tonality}")

        i += 1

    for a in ans:
        print(a)


main()
