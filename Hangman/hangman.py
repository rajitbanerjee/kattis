"""https://open.kattis.com/problems/hangman"""

word = input()
guesses = input()

chances, correct = 10, 0

for g in guesses:
    if g not in word:
        chances -= 1
    else:
        correct += 1

    if correct == len(set(word)):
        print("WIN")
        break
    if chances == 0:
        print("LOSE")
        break
    