"""https://open.kattis.com/problems/licensetolaunch"""

_ = input()
junk = list(map(int, input().split()))
print(junk.index(min(junk)))