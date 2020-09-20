#Multiple Inheritance diamond condition
class A:
    def method(self):
        print("Belongs to A")
class B(A):
    def method(self):
        print('Belongs to B')
class C(A):
    def method(self):
        print('Belongs to C')
class D(B,C):
    pass
d=D()
d.method()
