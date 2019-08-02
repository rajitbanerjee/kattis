"""https://open.kattis.com/problems/mjehuric"""

nums = list(map(int, input().split()))

def display(nums):
    for n in nums:
        print(n, end=' ')
    print()

def checkAndSwap(i1, i2, nums):
    if nums[i1] > nums[i2]:
        nums[i1], nums[i2] = nums[i2], nums[i1]
        display(nums)
    return nums

while nums != [1, 2, 3, 4, 5]:
    for i in range(4):
        nums = checkAndSwap(i, i+1, nums)
