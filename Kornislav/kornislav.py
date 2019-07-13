"""https://open.kattis.com/problems/kornislav"""

nums = list(map(int, input().split()))
nums.remove(max(nums))

print(min(nums) * max(nums))
