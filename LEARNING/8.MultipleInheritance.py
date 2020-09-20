class OS:
    multitasking=True
    name="Mac Os"
class Apple:
    website='www.apple.com'
    name="Apple"
class MacBook(OS,Apple):
    def __init__(self):
        if self.multitasking is True:
            print('Hi, this is made by {}'.format(self.website))
            print(self.name)
            #order decides which to prefer in multiple inheritance
mac=MacBook()
