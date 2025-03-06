# Write a program to find the HCF of two numbers without using recursion.

def hcf_of_2num(a,b):

    while b:
        a,b=b,a%b
    return a    

a=int(input('enter num1: '))
b=int(input('enter num2: '))

print(hcf_of_2num(a,b))