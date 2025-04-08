def gradeCaculator(num):
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