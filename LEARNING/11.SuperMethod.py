#addition between two numbers is overriding
class Employee:
    def setNoOfWorkingHours(self):
        self.noOfWorkingHours=40
    def displayNoOfWorkingHours(self):
        print(self.noOfWorkingHours)
class Trainee(Employee):
    def setNoOfWorkingHours(self):
        self.noOfWorkingHours=45
    def resetNoOfWorkingHours(self):
        super().setNoOfWorkingHours()
employee=Employee()
employee.setNoOfWorkingHours()
employee.displayNoOfWorkingHours()
trainee=Trainee()
trainee.setNoOfWorkingHours()
trainee.displayNoOfWorkingHours()
trainee.resetNoOfWorkingHours()
trainee.displayNoOfWorkingHours()
