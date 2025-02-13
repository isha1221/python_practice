# Fibonacci Series Generator
# Question: Write a Python function fibonacci(n) that generates the first n terms of the Fibonacci sequence.

# The Fibonacci sequence starts as 0, 1, 1, 2, 3, 5, 8..., where each term is the sum of the two previous ones.
# Use this function to print the first n Fibonacci numbers.
# Example Input/Output:

# Enter a number: 6
# Fibonacci sequence: [0, 1, 1, 2, 3, 5]

def fib(number):
     
    i,j=0,1
    fib_sequ=[]
    for i in range(0,number):
        fib_sequ.append(i)
        i,j=j,i+j
        # print(i,j)
    return fib_sequ    
number= int(input('enter a number :'))        

print(fib(number))        
