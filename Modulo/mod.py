"""https://open.kattis.com/problems/modulo"""

nums = set()
for _ in range(10):
    nums.add(int(input()) % 42)

print(len(nums))