class Employee:
    noOfWorkingHours=40
employee1=Employee()
employee2=Employee()
print(employee1.noOfWorkingHours)
print(employee2.noOfWorkingHours)
Employee.noOfWorkingHours=45
print(employee1.noOfWorkingHours)
print(employee2.noOfWorkingHours)
employee1.name='John'
employee2.name='Tom'
#Error if not created for second instance
print(employee1.name)
print(employee2.name)
employee1.noOfWorkingHours=40
print(employee1.noOfWorkingHours)
print(employee2.noOfWorkingHours)
