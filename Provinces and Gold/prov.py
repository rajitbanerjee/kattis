"""https://open.kattis.com/problems/provincesandgold"""

from collections import OrderedDict
vic, tres = OrderedDict(), OrderedDict()
vic = {"Province": 8, "Duchy": 5, "Estate": 2}
tres = {"Gold": 6, "Silver": 3, "Copper": 0}

inp = list(map(int, input().split()))
money = inp[0] * 3 + inp[1] * 2 + inp[2]

options = []
for coin, cost in tres.items():
    if money >= cost:
        options.append(coin)
        break

for prov, cost in vic.items():
    if money >= cost:
        options.insert(0, prov)
        break

if len(options) == 2:
    print(options[0], "or", options[1])
else:
    print(options[0])        




