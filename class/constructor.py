############################ Class Definition ###################################################
class Employee:
    name = None
    company = None
    salary = None
    ################################## Constructor ##################################
    def __init__(self,name,company,salary):
        self.name = name
        self.company = company
        self.salary = salary
    ################################## Constructor ##################################
    def printData(self):
        print("Name is: "+ self.name+"\nCompany is: "+self.company+"\nSalary is : "+str(self.salary))

############################ Class Definition ###################################################

newEmp = []

n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter your name: ")
    company = input("Enter your company name: ")
    salary = int(input("Enter your salary: "))
    emp = Employee(name,company,salary)
    newEmp.append(emp)

for emp in newEmp:
    emp.printData()