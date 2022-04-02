################################## Base/Parent class #######################################
class Person:
    name = None
    def __init__(self):
        self.name = input("enter your name: ")
    def getData(self):
        print("Name is :"+ self.name)
################################## Base/Parent class #######################################

############################# Child class of Person class ###################################  
class Employee(Person):
    company = None
    def __init__(self):
       super().__init__()
       self.company = input("Enter your company: ")
    def getData(self):
       super().getData() 
       print("Company is :"+self.company)
############################# Child class of Person class ###################################   

############################# Child class of Employee class #################################   
class Programmer(Employee):
    language = None
    def __init__(self):
        super().__init__()
        self.language = input("enter your language: ")
    def getData(self):
        super().getData()
        print("Language is : "+ self.language)
############################# Child class of Employee class ################################# 

obj1 = Programmer()
obj1.getData()


