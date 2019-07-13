"""https://open.kattis.com/problems/ptice"""

from math import ceil

N = int(input())
correct = input()

adrian = ("ABC" * ceil(N/3))[:N]
bruno = ("BABC" * ceil(N/4))[:N]
goran = ("CCAABB" * ceil(N/6))[:N]

freq = {"Adrian": 0, "Bruno": 0, "Goran": 0}
for i in range(N):
    if adrian[i] == correct[i]:
        freq["Adrian"] += 1
    if bruno[i] == correct[i]:
        freq["Bruno"] += 1
    if goran[i] == correct[i]:
        freq["Goran"] += 1
        
print(max(freq.values()))
for name, score in freq.items():
    if score == max(freq.values()):
        print(name)






