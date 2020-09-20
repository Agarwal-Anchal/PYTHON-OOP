#Check if an Employee has met his daily target or not: 5 sales a week
class Employee:
    name='Ben'
    designation='Sales Executive'
    salesmadethisweek=6
    def hasAchievedTarget(self):
        if self.salesmadethisweek >=5:
            print('Sales Target has been achieved')
        else:
            print('Traget has not been achieved')
employeeOne=Employee()
print(employeeOne.name)
employeeOne.hasAchievedTarget()
