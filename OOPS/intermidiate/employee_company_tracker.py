# Problem: Employee and Company Tracker
# Prompt:
# Create an Employee class with a class attribute company = "TechCorp".

# Each employee has a name and position

# Show how changing the class attribute vs instance attribute affects the output

# Follow-up:
# Use class and instance methods to interact with the company attribute.

class Employee():
    company = "TechCorp" #class atribute
    def __init__(self,name,position):
        self.name=name #instance atrribute
        self.position=position
        pass
    def display(self):
        print(f'name: {self.name}')
        print(f'position: {self.position}')
        print(f'company: {self.company}')#this will be instance attribute
        return None
name=input('enter your name: ')
position=input('enter your position')  
emp=Employee(name,position) 
print(emp.display())

# class Employee:
#     # Class attribute
#     company = "TechCorp"

#     def __init__(self, name, position):
#         self.name = name        # Instance attribute
#         self.position = position

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Position: {self.position}")
#         print(f"Company (instance): {self.company}")

#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company

#     @staticmethod
#     def company_info():
#         print("This is a tech company focusing on AI and Robotics.")

# # Input
# name = input("Enter your name: ")
# position = input("Enter your position: ")

# # Create an instance
# emp1 = Employee(name, position)

# # # Display original details
# # print("\n--- Original Employee Info ---")
# # emp1.display()

# # # Change instance attribute (only affects this instance)
# # emp1.company = "StartUpX"
# # print("\n--- After Changing Instance's Company Attribute ---")
# # emp1.display()

# # # Create a second instance to show class attribute remains the same
# # emp2 = Employee("Alice", "Engineer")
# # print("\n--- Second Employee Info (Still uses class attribute) ---")
# # emp2.display()

# # # Change class attribute using class method
# # Employee.change_company("FutureTech")
# # print("\n--- After Changing Class Attribute via Class Method ---")
# # emp2.display()

# # # Show static method usage
# # print("\n--- Company Info ---")
# # Employee.company_info()
