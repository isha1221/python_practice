# # # Write a function to find the longest word in a sentence.


def longest_word(sentence):
    max=0
    long_word=""
    for word in sentence.split():
    #  w = [len(word) ] 
    #  print(w)
        if(len(word)>max):
            max=len(word)
            long_word=word
    
    return long_word       
    

sentence=input('enter a sentence: ')

print(longest_word(sentence))



