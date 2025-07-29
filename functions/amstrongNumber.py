# Armstrong Number Checker
# Question: Write a function is_armstrong(n) that checks if a number is an Armstrong number.

# An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
# Example: 153 → 1³ + 5³ + 3³ = 153 (so it's an Armstrong number).
# Example Input/Output:

# Enter a number: 153
# 153 is an Armstrong number.

# def is_armstrong(n):
#     s=str(n)
#     raise_to=len(s)
#     for i in s:
#         if sum(int(i)**raise_to)==n:
#             print('is armstrong')
#             return True
#         else:
#             return False

# n=int(input('enter a number: '))

# print(is_armstrong(n))

# the problem in the above logic is that sum requires atleast 2 numbers but here it is unable to get it i.e sum() expects a list or generator, but int(i)**raise_to is a single value.



def is_armstrong(number):
    num_str = str(number)
    n = len(num_str)  # Get the number of digits
    armstrong_sum = sum(int(digit) ** n for digit in num_str)  # Calculate sum of digits^n
    return armstrong_sum == number

# Example Usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is NOT an Armstrong number.")



def missing_num(nums):
    nums=sorted(nums)
    n=len(nums)
    for i in range(n+1):
        if i not in nums:
            print(i)
            return i    
nums=[1,2,3,6,7,5,0,9,4]
missing_num(nums)

def missing_num(nums):
    # nums=sorted(nums)
    n=len(nums)
    ans=sum(range(n+1))-sum(nums) 
    print(ans) 
         
nums=[1,2,3,6,7,5,0,9,4]
missing_num(nums)