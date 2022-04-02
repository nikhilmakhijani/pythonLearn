################################## Base/Parent class #######################################
class Person:
    name = None
    def __init__(self):
        self.name = input("enter your name: ")
    def getData(self):
        print("Name is : "+ self.name)
################################## Base/Parent class #######################################

################################## Base/Parent class #######################################
class Employee:
    company = None
    def __init__(self):
        self.company = input("enter your company: ")
    def getData(self):
        print("Company is : "+ self.company)
################################## Base/Parent class #######################################

################################## Child/derived class #####################################
class Programmer(Person, Employee): 
    language = None
    def __init__(self):
        super().__init__() # will call constructor of class Person 
        Employee.__init__(self) 
        self.language = input("enter your language: ")
    def getData(self):
        super().getData()
        Employee.getData(self)
        print("Language is : "+ self.language)
################################## Child/derived class #####################################

obj1 = Programmer()
obj1.getData()

