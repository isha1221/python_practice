# Write a function to determine if a number is a Narcissistic number 
# (sum of each digit raised to the power of the number of digits equals the number itself).

# 1^3 + 5^3 + 3^3 = 153

# number = 12345



def nar_num(number):
    num_str=str(number)
    sum=0
    for digit in num_str:
    #    print(int(digit))
       sum+=int(digit)**len(num_str)
    # print(sum)
    if(sum==number):
        print('is a Narcissistic number')
    else:
        print('not a Narcissistic')    

number=int(input('enter a num: '))       

nar_num(number)