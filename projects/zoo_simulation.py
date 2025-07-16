# Zoo Simulation – OOP Problem Statement
# 🎯 Objective:
# Design and implement a zoo simulation system using Object-Oriented Programming in Python.
# The system should model different types of animals, their behaviors, and their enclosures, 
# allowing for realistic interaction and reporting of zoo status.

# 🧩 Key Requirements:
# 1. Animal Hierarchy (Inheritance)
# Create a base class Animal with common attributes and methods:
# name
# age
# species
# make_sound()
# feed()
# Then create subclasses for specific animals:
# Lion, Elephant, Monkey, Parrot, etc.
# Each subclass should override the make_sound() and feed() methods with unique implementations.

# 2. Enclosure Class (Composition)
# Create a class Enclosure which:

# Has a name (e.g., "Savannah Zone", "Bird House")

# Can contain multiple animals (list of Animal objects)

# Has methods to:

# add_animal()

# list_animals()

# feed_all_animals()

# 3. Zoo Class (Composition of Enclosures)
# Create a Zoo class to:

# Hold multiple Enclosure objects

# Have methods to:

# add_enclosure()

# zoo_status() (print names of enclosures and animals in them)

# feed_all_animals() (call feed on all animals in all enclosures)

class Animal():
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
        pass
    def make_sound(self):
        print(f"{self.name} makes a generic sound")
        pass
    def feed(self):
        print(f"{self.name} eats something")
        pass
    
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars")
        pass
    def feed(self):
        print(f'{self.name} eats meat')
        pass
      
class Monkey(Animal):
    def make_sound():
        print('roar')
        pass
    def feed():
        print('flesh')
        pass
     
class Elephant(Animal):
    def make_sound():
        print('trumph')
        pass
    def feed():
        print('grass')
        pass
        
class Parrot(Animal):
    def make_sound():
        print('chirp')
        pass
    def feed():
        print('guava')
        pass            
    

lion=lion()
lion.make_sound()
lion.feed()
parrot=parrot()
parrot.feed()
parrot.make_sound()
elephant= elephant()
elephant.feed()
elephant.make_sound()   

#   inheritance parent and child relation:
class a():
    def feature1():
        print("feature 1 work")
    def feature2():
        print('feature 2 working')
        
a=feature1()
                   
              