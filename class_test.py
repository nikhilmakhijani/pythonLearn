class Employee:
    company = "mine"

newEmp = Employee()
print(newEmp.company)
Employee.company ="yours"
print(newEmp.company)
