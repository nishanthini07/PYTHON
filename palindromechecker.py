word = input("What is the word?: ")

def word_checking(word):
    word[::-1]
    return word[::-1]
checking_word = word_checking(word)

if word == checking_word:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")