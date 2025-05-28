# Prompt:
# Write a Dog class with name and breed. 
# Override the __str__ method to return a formatted string, e.g., 
# "Dog(name=Fido, breed=Labrador)".

class dog():
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        pass
    def __str__(self):
        return f'Dog {self.name} has breed {self.breed}'
        
    
dog_real=dog("fido","Labrador")
print(str(dog_real))    