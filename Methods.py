# methods are function that belongs to object
"""
class Student:
    def __init__(self,name):
     self.name=name 
     
    def hello(self):
         print("HEllo ",self.name)
         
s1=Student("Awais")
s1.hello()
"""
         
class Student:
    def __init__(self,name,marks):
     self.name=name 
     self.marks=marks
     
    def hello(self):
         print("HEllo ",self.name)
   
    def getmarks(self):
        return self.marks
         
s1=Student("Awais",97)
s1.hello()     
print(s1.getmarks())