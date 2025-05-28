# 4. Problem: Rectangle Factory Method

# Prompt:
# Create a Rectangle class with attributes width and height, and methods:
# area()
# perimeter()

# Add:
# A class method square(cls, side) that returns a rectangle with equal width and height.

class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
        # pass
    def area(self):
        return self.height*self.width
         
    def perimeter(self):
       return 2*(self.height+self.width)
    
    @classmethod    
    def square(cls,side):
       return cls(side,side)
    
reactangle_param=Rectangle(20,40)
print(f"area: {reactangle_param.area()}, perimeter: {reactangle_param.perimeter()}")

square_param= Rectangle.square(10)  
print(f"square- area: {square_param.area()}, perimeter: {square_param.perimeter()}") 