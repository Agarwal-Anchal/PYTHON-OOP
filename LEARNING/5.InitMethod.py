class Employee:
    def __init__(self,name):
        self.name=name
    #def enterDetails(self):
        #self.name='Mark'
    def displayDetails(self):
        print(self.name)
employee=Employee('Mark')
#employee.enterDetails()
#If we did not call first method second method threw error
#So create init
employee.displayDetails()
employee2=Employee('Mathew')
employee2.displayDetails()
