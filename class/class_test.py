class Employee:
    name = None
    company = "mine"
    salary = None


newEmp = Employee()
print(newEmp.company)
Employee.company ="yours" 
print(newEmp.company) # will print "yours"

n = int(input("Enter the number of employees"))
for i in range(n):
    newEmp[i] = Employee()

for emp in newEmp:
    print(emp)
