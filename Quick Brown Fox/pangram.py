"""https://open.kattis.com/problems/quickbrownfox"""

import string

def checkPangram(phrase):
    missing = ""
    for letter in string.ascii_lowercase:
        if letter not in phrase:
            missing += letter
    
    if missing == "":
        return "pangram"
    else:
        return "missing " + missing

ans = []
for _ in range(int(input())):
    phrase = input()
    ans.append(checkPangram(phrase.lower()))

for a in ans:
    print(a)
