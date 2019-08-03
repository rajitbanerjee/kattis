"""https://open.kattis.com/problems/mirror"""

T = int(input())
ans = []

def doubleMirror(image, R, C):
    mirror_im = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            mirror_im[R - i - 1][C - j - 1] = image[i][j]
    
    for i in range(R):
        mirror_im[i] = "".join(mirror_im[i])

    return "\n".join(mirror_im)

for _ in range(T):
    R, C = map(int, input().split())
    image = []
    for _ in range(R):
        row = list(input())
        image.append(row)
    
    ans.append(doubleMirror(image, R, C))

for i, a in enumerate(ans):
    print(f"Test {i + 1}")
    print(a)