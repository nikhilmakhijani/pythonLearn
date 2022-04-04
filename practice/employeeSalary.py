from curses.ascii import EM
from os import name


class Employee:
    name = None
    salary = None
    increment =  None

    def __init__(self):
        self.name = input("Enter employee name: ")
        self.salary = float(input("Enter employee salary: "))
        self.increment = float(input("Enter employee increment: "))
    
    @property
    def salaryAfterIncrement(self):
        self.salary += (self.salary * self.increment)/100
        return self.salary

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSal):
       self.increment = (newSal - self.salary)/self.salary * 100
    
    def getInfo(self):
        print("Name is: "+self.name)
        print("Salary is: "+str(self.salary))
        print("Increment is "+str( "%.2f" % self.increment)+"%")
    
def main():
    emp1 = Employee()
    print(emp1.salaryAfterIncrement)
    emp1.getInfo()
    emp1.salaryAfterIncrement = 122000
    emp1.getInfo()

if __name__ == '__main__':
    main()
     

    

