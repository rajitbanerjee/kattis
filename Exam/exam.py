"""https://open.kattis.com/problems/exam"""

k = int(input()) # Friend's correct answers
my_ans = list(input())
fr_ans = list(input())

same, total = 0, len(my_ans)
for i in range(total):
    if my_ans[i] == fr_ans[i]: 
        same += 1

if same < k:
    print(total + same - k)
else:
    print(total - same + k)