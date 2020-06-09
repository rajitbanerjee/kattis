"""https://open.kattis.com/problems/oktalni"""

num = int(input())
print(oct(int(f"0b{num}", base=2))[2:])
