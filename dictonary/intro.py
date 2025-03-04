##NOTE:
# dictionary is a mutable and unordered
# Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.


myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# this dictionary’s keys are 'size', 'color', and 'disposition'. The values for these keys are 'fat', 'gray', and 'loud', respectively. 

##accessing element of the dictionary
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')


##NOTE: Dictionaries can still use integer values as keys,
# just like lists use integers for indexes, 
# but they do not have to start at 0 and can be any number.
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam)