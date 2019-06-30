"""https://open.kattis.com/problems/spavanac"""

H, M = list(map(int, input().split()))
if H == 0:
    H = 24
# convert H and M to mins - 45 mins
mins = H * 60 + M - 45
# convert them back to 24 hour notation
H = mins // 60
M = mins % 60 
print(H, M)




