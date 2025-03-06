# keys(), values(), and items()

spam = {'color': 'red', 'age': 42}
for v in spam.values():
  print(v)


for k in spam.keys():
  print(k)


for i in spam.items():
  print(i)
  
  
##NOTE: the values in the dict_items value returned by the items() method are tuples of the key and value



spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
  print('Key: ' + k + ' Value: ' + str(v))  
  
  
  
##in not in Operators
spam = {'name': 'Zophie', 'age': 7}
print('name' in spam.keys())

print('color' not in spam.keys())  
  
  
  
##get() Method
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')  
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
#here 0 is the default value now eggs is not present in the dictionary so it will take the defult value

##setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white') ## color is not changed it remains default black
print(spam)