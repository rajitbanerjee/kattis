"""https://open.kattis.com/problems/autori"""

def main():
    paper = input().split('-')

    ans = ""
    for name in paper:
        ans += name[0]
    
    print(ans)

if __name__ == '__main__':
    main()
     