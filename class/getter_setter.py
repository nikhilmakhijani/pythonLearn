
class Employee:
    name = None
    salary = None
    salaryBonus = None
    def __init__(self):
        self.name = input("Enter your name: ")
        self.salary = int(input("Enter {} current salary: ".format(self.name)))
        self.salaryBonus = int(input("Enter {} current Salary Bonus: ".format(self.name)))
    # Getter 
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    # Setter
    @totalSalary.setter
    def totalSalary(self, updatedSalary):
         self.salaryBonus = updatedSalary - self.salary

obj1 = Employee()
print("Total Salary is :"+str(obj1.totalSalary))

obj1.totalSalary = 100000
print("Updated Salary bonus is :"+str(obj1.salaryBonus))
