# Write a function to check if a number is a perfect number (equal to the sum of its divisors).

def is_perfect_number(n):
    divisors = set()  # Using a set to avoid duplicates
    for i in range(1, int(n**0.5) + 1): 
        # n**0.5 is square root of n
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i) 
            # When i=2, 𝑛//𝑖=36//2=18 here 18 is also a divisor so it should also be added 
    if (sum(divisors)-n)==n:
        print('Bravoooo!! it is a perfect number')
        return True
    else:
        print('Sorry!! not a perfect number')
        return False
    
n=int(input('enter a number and check weather it is a perfect number of not: ')) 

is_perfect_number(n)
