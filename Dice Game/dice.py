"""https://open.kattis.com/problems/dicegame"""

gunnar = list(map(int, input().split()))
emma = list(map(int, input().split()))

def getAvgSum(lst):
    sumsLst = []
    for i in range(lst[0], lst[1] + 1):
        for j in range(lst[2], lst[3] + 1):
            sumsLst.append(i + j)
    
    return (sum(sumsLst)/len(sumsLst))

if getAvgSum(gunnar) > getAvgSum(emma):
    print("Gunnar")
elif getAvgSum(gunnar) < getAvgSum(emma):
    print("Emma")
else:
    print("Tie")
