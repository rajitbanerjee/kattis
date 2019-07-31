"""https://open.kattis.com/problems/runlengthencodingrun"""

(do, msg) = input().split()

def encode(msg):
    ans, chars = "", ""
    parts = []
    msg += " "
    
    for i in range(len(msg) - 1):
        if msg[i] == msg[i+1]:
            chars += msg[i]
        else:
            chars += msg[i]
            parts.append(chars)
            chars = ""

    for p in parts:
        ans += p[0] + str(len(p))
    print(ans)

def decode(msg):
    ans = ""
    for i, ch in enumerate(msg):
        if i % 2 == 0:
            ans += ch * int(msg[i + 1])
    print(ans)


if do == "E":
    encode(msg)
else:
    decode(msg)