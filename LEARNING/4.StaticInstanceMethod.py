class  Employee:
    def employeeDetails(self):
        self.name='Ben'
        #have to pass and dont want to use it anywhere in the function
        #Make it static
    @staticmethod
    def welcomeMsg():
        print("Welcome here!")
employee=Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMsg()
