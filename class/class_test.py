class Employee:
    name = None
    company = "mine"
    salary = None


newEmp = Employee()
print(newEmp.company)
Employee.company ="yours" 
print(newEmp.company) # will print "yours"
