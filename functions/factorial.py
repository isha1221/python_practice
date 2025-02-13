# Question: Factorial Calculator
# Write a Python program that calculates the factorial of a given number using a function.

# Define a function factorial(n) that returns the factorial of n.
# Use this function to compute the factorial of a user-input number.
# Ensure the function correctly handles edge cases like n = 0 (since 0! = 1).
# Example Input/Output:

# Enter a number: 5
# Factorial of 5 is 120.

# Enter a number: 0
# Factorial of 0 is 1.

def factorial(number):
    result =1

    for result in range(1,number):
        result*=number
    return result
number= int(input('enter a number :'))  



print(factorial(number))