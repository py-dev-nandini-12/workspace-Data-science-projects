word = input('Enter a word :')
word.lower()

new_word = (word.lower()[::-1])

if new_word == word:
    print('The word is a plaindrome')
else:
    print('The word is not a palindrome')