"""https://open.kattis.com/problems/datum"""

D, M = map(int, input().split())
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 01/01/2009 was a Thursday
day = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

total_days = 0
for i in range(M):
    total_days += months[i]
total_days += D

print(day[total_days % 7 - 1])
