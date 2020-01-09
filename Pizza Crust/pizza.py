"""https://open.kattis.com/problems/pizza2"""

R, C = map(int, input().split())
print(100 * pow(1 - C/R, 2))