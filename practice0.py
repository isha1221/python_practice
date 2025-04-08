# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
#     def __str__(self):
#         return f"Dog(name={self.name}, age={self.age}, species={self.species})" # adding this allows us to print the output in human readable format
    
# miles = Dog("Miles", 4)

# print(miles.description(),

# miles.speak("Woof Woof"),


#     miles.speak("Bow Wow"))

# print(miles)

class Car():
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
        
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles" 

car1= Car(color="blue",mileage=20_000)  
print(car1)

car2= Car(color="red",mileage=30_000) 
print(car2)     