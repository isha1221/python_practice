# Design a Car class that represents a real-world car. The class should have attributes: make, model, and year.
# It should include a method start_engine() that prints "The <year> <make> <model> is starting."

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        pass
    def start_engine(self):
        return f"The {self.year} {self.model} {self.make} is starting"
    
car=Car("is","mh02","1961")
print(car.start_engine())