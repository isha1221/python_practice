
# Question: Palindrome Checker
# Write a Python program that checks whether a given string is a palindrome or not.

# Define a function is_palindrome(text) that returns True if the input string is a palindrome and False otherwise.
# Ignore case sensitivity (e.g., "Madam" and "madam" should be considered palindromes).
# Ignore spaces (e.g., "nurses run" should be considered a palindrome).

# Example Input/Output:
# Enter a word or phrase: madam
# "madam" is a palindrome.

# Enter a word or phrase: Hello
# "Hello" is not a palindrome.

# Enter a word or phrase: Was it a car or a cat I saw
# "Was it a car or a cat I saw" is a palindrome.


def palindrome(word):
#     for n in range(1,word.lenght):
#         if(word[1]==word[word.lenght-1]):
    word = word.replace(" ", "").lower()

    # Compare original string with its reverse
    if word == word[::-1]:
            print('is a palindrome')
            return True
    else:
           print('not a palindrome')
           return False
word=input('enter a word or a sentence: ')  

print(palindrome(word))
            