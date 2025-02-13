# #globle scope and local scope 
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# def spam():
#   global eggs # eggs is a global variable
#   eggs = 'spam'

# eggs = 'global'
# spam()# here spam is called and in spam eggs is gobal var so it is printing egggs from the spam function    
# print(eggs)





#4 rules to check weather the var is global or local
def spam():
  global eggs
  eggs = 'spam' # this is the global

def bacon():
  eggs = 'bacon' # this is a local
#   because there’s an assignment statement for it in that function

def ham():
  print(eggs) # this is the global
#   because there is no assignment statement or global statement for it in that function.

eggs = 42 # this is the global
spam()
print(eggs)