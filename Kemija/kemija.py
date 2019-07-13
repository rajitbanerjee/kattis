"""https://open.kattis.com/problems/kemija08"""

sent, ans, i = input(), "", 0
while i < len(sent):
    if sent[i] in ['a', 'e', 'i', 'o', 'u']:
        i += 2
    ans += sent[i]
    i += 1
print(ans)