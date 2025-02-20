import random


cat=['fluffy','white','persian']

# shuffle the list
random.shuffle(cat)
print(cat) 

print('random number in a given range ') 
print(random.randint(0,10))

print('returns multiple random elements from the list') 
print(random.choices(cat,k=5))

print('random floating value within the range(low,high,mode)') 
print(random.triangular(10,100,20))

print('random floating number bteween given range both inclusive') 
print(random.uniform(4,9))

print('single random value from list') 
print(random.choice(cat))

