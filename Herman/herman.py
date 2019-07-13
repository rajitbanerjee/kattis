"""https://open.kattis.com/problems/herman"""

from math import pi

R = int(input())

# circle becomes a square with edge = sqrt(2 * r)
def taxicab(R):
    return 2 * R * R
    
def euclidian(R):
    return pi * R * R

print(f"{euclidian(R)}\n{taxicab(R)}")

