class Car:
    def __init__(self,cars):
        self.cars=cars
        self.cost=0
    def FareDetails(self,car,days):
        if car =='Hatchback':
            self.cost=30*days
            print("Fare is"+str(elf.cost))
        elif car =='Sedan':
            self.cost=50*days
            print("Fare is"+str(self.cost))
        elif car =='SUV':
            self.cost=100*days
            print("Fare is"+str(self.cost))
        else:
            print('We cannot get you this car')
class Customer:
    def tellCar(self):
        print("Enter car:")
        self.car=input()
        print('Enter days:')
        self.days=int(input())
        return self.car,self.days
car=Car(['Hatchback','Sedan','SUV'])
cust=Customer()
while(True):
    print("Want to rent a car? Enter 1")
    choice=int(input())
    if choice==1:
        print('Enter details of the car you want to buy:')
        cars,days=cust.tellCar()
        car.FareDetails(cars,days)
    else:
        quit()
