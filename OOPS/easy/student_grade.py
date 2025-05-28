# Attributes: name, grades (list)
# Method: average() that returns average of grades

class students():
    def __init__(self,name:str,grades:list):
        self.name=name
        self.grades=grades
        pass
    def avrage(self):
        total=sum(self.grades)
        count=len(self.grades)
        avg=total/count
        return avg
    def __str__(self):
        return f'{self.name} have average score of {self.avrage()}'
        
avrage_grade=students("isha",[30,40,50])
print(avrage_grade.avrage())
print(str(avrage_grade))  
print(avrage_grade)      
            
            
        
        
        
        
        
        
        