"""https://open.kattis.com/problems/humancannonball2"""

import math

def main():
    N = int(input()) # number of test cases
    safety = []
    for i in range(N):
        param = list(map(float, input().split()))
        safety.append(testSafe(param))
    
    for each in safety:
        print(each)

def testSafe(param):
    v0, theta, x1, h1, h2 = param
    theta = math.radians(theta)
    
    t = x1 / (v0 * math.cos(theta))
    y = v0 * t * math.sin(theta) - 0.5 * 9.81 * (t**2)

    if y - 1 >= h1 and y + 1 <= h2:
        return "Safe"
    else:
        return "Not Safe"



if __name__ == '__main__':
    main()
