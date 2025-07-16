# Problem Statement:
# To speed up his composition of generating unpredictable rhythms, Blue Bandit wants the list of prime numbers available 
# in a range of numbers. Can you help him out?
# Write a python program to print all prime numbers in the interval (a and b, both inclusive).
# Note:
# Input 1 should be lesser than Input 2. Both the inputs should be positive.
# Range must always be greater than zero.
# If any of the condition mentioned above fails, then display "Provide valid input"
# Use a minimum of one for loop and one while loop
# Given your Sample Input 1:
# 2
# 15

# The expected Sample Output 1 is:
# 2 3 5 7 11 13 


def prime(a,b):
    l=[]
    if(a<b):
        for i in range(a,b):
            if isprim(i):
                return l.append(i)
            else:
                i+=1
def isprim(i):
    while(b>i>1):
        if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0):
            print('is prme')
            return True
        else:
            print('not prime')  
            return False  
        
a=int(input()) 
b=int(input())

print(prime(a,b))               