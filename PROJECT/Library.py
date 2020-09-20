class Library:
    def __init__(self,books):
        self.inventory=books
    def lendBook(self,request_book):
        if(request_book not in self.inventory):
            print("sorry, this book is not there")
        else:
            print('You have taken the book')
            self.inventory.remove(request_book)
    def addBook(self,return_book):
        print('Book is added back to Library')
        self.inventory.append(return_book)
    def printBook(self):
        print('Available Books are:')
        for i in self.inventory:
            print(i+" ")
class Customer:
    def requestBook(self):
        print('Enter the name of book you want:')
        self.book=input()
        return self.book
    def returnBook(self):
        print('Enter the book you want to return:')
        self.book=input()
        return self.book
library=Library(['ABC','DEF','GHI'])
customer=Customer()
while(True):
    print('Enter 1 to display all books')
    print('Enter 2 to request for a book')
    print('Enter 3 to return a book')
    print('Enter 4 to exit')
    entered=int(input())
    if entered==1:
        library.printBook()
    elif entered==2:
        requested=customer.requestBook()
        library.lendBook(requested)
    elif entered==3:
        returned=customer.returnBook()
        library.addBook(returned)
    else:
        pass
