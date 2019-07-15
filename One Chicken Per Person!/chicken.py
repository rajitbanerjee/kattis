"""https://open.kattis.com/problems/onechicken"""

N, M = map(int, input().split())

diff = abs(N - M)

if M > N:
    if diff == 1:
        p = str(diff) + " piece"
    else:
        p = str(diff) + " pieces"
    print(f"Dr. Chaz will have {p} of chicken left over!")
else:
    if diff == 1:
        p = str(diff) + " more piece"
    else:
        p = str(diff) + " more pieces"
    print(f"Dr. Chaz needs {p} of chicken!")