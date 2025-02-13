# Write a function to check if a number is even or odd.

def is_even(n):
    if(n==0):
        print('it is neither odd nor even')
        return False
    if n%2==0:
        print('is even')
        return True
    else:
        print('is odd')
        return True 
n=int(input('enter the number: '))

is_even(n)

   