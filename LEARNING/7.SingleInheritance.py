class Apple:
    manufacturer='Apple Inc.'
    contact='www.apple.co/contact'
    def contactDetails(self):
        print('To contact us log on to',self.contact)
class Macbook(Apple):
    def __init__(self):
        self.yearOfManufacture=2017
    def manufactureDetails(self):
        print('This was made in year {} by {}'.format(self.yearOfManufacture,self.manufacturer))
macBook=Macbook()
macBook.manufactureDetails()
macBook.contactDetails()
