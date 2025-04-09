def gradeCaculator(num):
    """this is a document area where you can add what your function does also what 
    variable in the function is for so that it's easier to use it further in the code"""
    if(num>95):
        print('whoo you scored  A+')
        return True
    elif(80<num<95):
        print('whoo you scored  A')  
        return True
    elif(70<num<80):
        print('whoo you scored  B+') 
        return True
    elif(num<70):
        print('whoo you scored  B')  
        return True
                 
num=int(input("enter number between 1 to 100"))          
print(gradeCaculator(num))        
        
# print(gradeCaculator.__doc__)        

# lambda func

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))