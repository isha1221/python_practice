# Reverse a Sentence
# Question: Write a function reverse_sentence(sentence) that reverses the words in a sentence.

# Example Input/Output:
# Enter a sentence: Python is fun
# Reversed sentence: fun is Python


# def reverse_sentence(sentence):
#     rev_sequ=[]
    
#     for char in sentence:
#         rev_sequ.insert(0, char)  # Insert at the beginning of the list
#     return "".join(rev_sequ)
# sentence= input('enter your sentence: ')

# print(reverse_sentence(sentence))


# OR use slicing 
# sequence[start:stop:step]

def reverse_sentence(sentence):
    return sentence[1:1:-1]  # Reverse the string using slicing

sentence = input("Enter your sentence: ")

print("Reversed Sentence:", reverse_sentence(sentence))
