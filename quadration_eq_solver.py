import math

def eq(a,b,c):
    
    discriminant=b**2-4*a*c
    
    if discriminant < 0:
        print("No real solutions (complex roots)")
        return
    d1=((-b)+math.sqrt(discriminant))/2*a
    d2=((-b)-math.sqrt(discriminant))/2*a
    print(d1,d2)
    
a=int(input("enter a coeficient of x^2: ")) 
b=int(input("enter a coeficient of x: "))  
c=int(input("enter a constant of: "))

print(eq(a,b,c))     