"""https://open.kattis.com/problems/abc"""

def main():
    nums = list(map(int, input().split())) # given order of numbers
    order = input() # required order of numbers

    dic = {'A': 0, 'B': 0, 'C': 0}
    dic['A'] = min(nums)
    dic['C'] = max(nums)
    for i in nums:
        if i not in dic.values():
            dic['B'] = i
    
    for each in order:
        print(dic[each], end = ' ')

if __name__ == '__main__':
    main()
