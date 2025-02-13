# Question:
# Write a Python program that takes a positive integer as input and checks whether it is a prime number or not. Implement the prime-checking logic inside a function called is_prime(number), and then use this function in your main program to test user input.

# Example Input/Output:

# Enter a number: 7
# 7 is a prime number.

# Enter a number: 10
# 10 is not a prime number.

def isPrime(number):
    if(number<=0): 
        print('neither prime nor composite')       
        return None        
    if(number ==1):
        print('composite')
        return False   
    for enterNum in range(2,int(number**0.5) + 1):
        if number%enterNum==0:
            print('composite') 
            return False
    print('is prime')  
    return True   
while True:
    try:
     number =int(input('enter number: '))
     isPrime(number)
     break
    except ValueError:
        print('enter a number not a string') 



       