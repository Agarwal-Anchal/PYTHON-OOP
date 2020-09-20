class Employee:
    def employeeDetails(self):
        self.name='Mathew'
        print(self.name)
        #here age can't be accessed in another method
        age=20
        print(age)
    def printDetails(self):
        print('Another'+self.name)
        print('Another'+age)
employee =Employee()
employee.employeeDetails()
Employee.employeeDetails(employee)
employee.printDetails()
