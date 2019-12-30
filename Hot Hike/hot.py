"""https://open.kattis.com/problems/hothike"""

_ = input()
forecast = list(map(int, input().split()))

t_min, pos = max(forecast), 0
for i in range(0, len(forecast) - 2):
    # get the max temperature of the 2 hiking days
    max_t = max(forecast[i], forecast[i + 2])
    if max_t < t_min:
        # get the lowest of the max temperatures
        t_min = max_t
        pos = i
    
print(pos + 1, t_min)