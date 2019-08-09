"""https://open.kattis.com/problems/babybites"""

_ = input()
words = input().split()

for i, w in enumerate(words):
    if w != "mumble" and w != str(i + 1):
        print("something is fishy")
        exit()

print("makes sense")