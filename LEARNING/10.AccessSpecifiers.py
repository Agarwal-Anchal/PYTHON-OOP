#Public member name without changes
#Protected start with _membername
#Private start with __membername
class Car:
    noOfWheels=4
    _color='Black'
    __yearOfManufacture=2017 #internally _car then __yearOfManufacture
class BMW(Car):
    def __init__(self):
        print('Protected',self._color)
car=Car()
print('Public',car.noOfWheels)
bmw=BMW()
print('Private',car._Car__yearOfManufacture)
#cannot print car.__yearOfmanufacture
