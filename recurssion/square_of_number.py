def square_num(num,power):
    if power==0:
        return 1
    elif power>=1:
        return num*square_num(num,power-1)
    else:
        return 1/square_num(num,-power)
    
    
num=int(input("enter your number: "))
power=int(input("enter power: "))
print(square_num(num,power))
    
    
# ex.:
# square_num(2, 3)  = 2 * square_num(2, 2)
# square_num(2, 2)  = 2 * square_num(2, 1)
# square_num(2, 1)  = 2 * square_num(2, 0)
# square_num(2, 0)  = 1   # Base case
    