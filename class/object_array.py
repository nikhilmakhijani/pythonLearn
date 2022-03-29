############################ Class Definition ###################################################
class Employee:
    name = None
    company = None
    salary = None
    def getData(self):
        self.name = input("Enter your name: ")
        self.company = input("Enter your company name: ")
        self.salary = int(input("Enter your salary: "))
    def printData(self):
        print("Name is: "+ self.name+"\nCompany is: "+self.company+"\nSalary is : "+str(self.salary))

############################ Class Definition ###################################################

newEmp = []

n = int(input("Enter the number of employees: "))

for i in range(n):
    emp = Employee()
    emp.getData()
    newEmp.append(emp)

for emp in newEmp:
    emp.printData()