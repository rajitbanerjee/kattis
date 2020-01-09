"""https://open.kattis.com/problems/missingnumbers"""

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

if len(nums) == nums[-1]:
    print("good job")
else:
    for i in range(1, nums[-1] + 1):
        if i not in nums:
            print(i)