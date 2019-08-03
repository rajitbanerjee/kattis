"""https://open.kattis.com/problems/jobexpenses"""

_ = input()

nums = list(map(int, input().split()))
expenses = sum([-i for i in nums if i < 0])
print(expenses)

