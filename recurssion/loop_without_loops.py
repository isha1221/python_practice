def looping(num,x):
    if(x>=num):   
       return
    print(x)       
    looping(num,x+1)
       
x=0        
num = 10      
looping(num,x)               