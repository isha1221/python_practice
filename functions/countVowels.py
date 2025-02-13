# Count Vowels in a String
# Question: Write a function count_vowels(text) that counts the number of vowels (a, e, i, o, u) in a given string.

# Example Input/Output:

# Enter a sentence: Hello World
# Number of vowels: 3



def count_vowels(text):
    count=0
    text=text.lower()
    for char in text:
        
        if char=='i' or char=='a' or char=='e' or char=='o' or char=='u' :
            count=count+1
    
    return count
          

text= input('enter your sentence: ')

print(count_vowels(text))

