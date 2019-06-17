"""
https://open.kattis.com/problems/aboveaverage
"""
def centAvg(grades) -> str:
    total = 0
    size = len(grades)
    avg = sum(grades)/size
    for mark in grades:
        if mark > avg:
            total += 1
    
    percent = round(total/size*100, 3)
    return "{:.3f}".format(percent) + "%"

def main():
    C = int(input())
    data = []
    for i in range(C):
        grades = list(map(int, input().split()))
        grades.pop(0)
        data.append(grades)
    
    for marks in data:
        print(centAvg(marks))

if __name__ == '__main__':
    main()