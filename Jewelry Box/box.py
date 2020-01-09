"""https://open.kattis.com/problems/jewelrybox"""

def maxVol(X, Y):
    # expression optained used calculus (maxima/minima)
    # the volume of the box is maximum when 'h' is minimum
    # dV/dh = XY - 4*h*(X + Y) + 12*h^2 = 0
    h = (X + Y - pow(X*X + Y*Y - X*Y, 0.5))/6
    return (X - 2*h) * (Y - 2*h) * h

def main():
    ans = []
    for _ in range(int(input())):
        X, Y = map(int, input().split())
        ans.append(maxVol(X, Y))
    
    for a in ans:
        print(a)

main()