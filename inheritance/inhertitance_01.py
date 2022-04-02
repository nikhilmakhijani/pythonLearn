from curses.ascii import EM


# Example of single inheritance

################################## Base/Parent class #######################################
class Person:
    name = None
    def __init__(self):
        self.name = input("enter your name: ")
    def getData(self):
        print("Name is :"+ self.name)
################################## Base/Parent class #######################################

################################# Child/derived class ######################################    
class Employee(Person):
    company = None
    def __init__(self):
       super().__init__()
       self.company = input("Enter your company: ")
    def getData(self):
       super().getData() 
       print("Company is :"+self.company)
################################# Child/derived class ######################################   
    

emp1 = Employee() # Creating object of Employee class
emp1.getData()

