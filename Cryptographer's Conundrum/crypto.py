"""https://open.kattis.com/problems/conundrum"""

cipher_text = input()

days = 0
for i in range(len(cipher_text)):
    if i % 3 == 0 and cipher_text[i] != 'P':
        days +=1 
    if i % 3 == 1 and cipher_text[i] != 'E':
        days += 1
    if i % 3 == 2 and cipher_text[i] != 'R':
        days += 1

print(days)

