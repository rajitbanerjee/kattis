"""https://open.kattis.com/problems/encodedmessage"""

T = int(input())

def decode(msg):
    n, index = int(len(msg)**0.5), 0
    # initialise matrix
    msg_matrix = [['0' for x in range(n)] for y in range(n)] 
    for col in range(n):
        for row in range(n - 1, -1, -1):
            # decode message by placing it in the matrix
            msg_matrix[row][col] = msg[index]
            index += 1 # move to next char in message

    new_msg = ""
    for i in range(n):
        for j in range(n):
            new_msg += msg_matrix[i][j]
    return new_msg
    
ans = []
for _ in range(T):
    msg = input()
    ans.append(decode(msg))
for a in ans:
    print(a)