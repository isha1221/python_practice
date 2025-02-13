# Write a function to return the square of a number.

def sqr_of_num(n):
    sqr_num=n**2
    return sqr_num
n=float(input('enter a number: ')) 
print(f'square of {n} is  {sqr_of_num(n):.4f}')
# :.4f exactly 4 digits after decimal