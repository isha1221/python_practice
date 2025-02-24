# NOTE:copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference

import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))

cheese = copy.copy(spam)
print(id(cheese)) # cheese is a different list with different identity.

cheese[1] = 42
print(spam)

print(cheese)

# NOTE: If the list you need to copy contains lists, then use the copy.deepcopy() 
# function instead of copy.copy(). The deepcopy() function will copy these inner lists a