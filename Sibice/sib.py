"""https://open.kattis.com/problems/sibice"""

N, W, H = list(map(int, input().split()))
dimensions = [W, H, (W*W + H*H)**0.5]
fits = []
for _ in range(N):
    flag = 0
    match = int(input())
    for i in dimensions:
        if match <= i:
            fits.append("DA")
            flag = 1
            break
    if flag == 0:
        fits.append("NE")

for ans in fits:
    print(ans)

    
    

