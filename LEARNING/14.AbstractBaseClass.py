from abc import ABCMeta,abstractmethod
#Shape object is not required at all
class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0
class Square(Shape):
    side=4
    def area(self):
        print(self.side*self.side)
class Rectangle(Shape):
    width=3
    length=10
    def area(self):
        print(self.width*self.length)
square=Square()
square.area()
rect=Rectangle()
rect.area()
