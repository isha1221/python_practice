# Write a function that counts the number of occurrences of a specific character in a string.

def countSpeciChar(word, char_to_count):
    count = 0
    for char in word:
        if char == char_to_count:
            count += 1
    return count

word = input('Enter a word or a sentence: ')
char_to_count = input('Enter the character to count: ')

result = countSpeciChar(word, char_to_count)

print(f"The character '{char_to_count}' appears {result} times in the given text.")