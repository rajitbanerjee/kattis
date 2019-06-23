"""https://open.kattis.com/problems/hissingmicrophone"""

def main():
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i+1] == 's':
            print("hiss")
            return
    print("no hiss")

if __name__ == '__main__':
    main()
