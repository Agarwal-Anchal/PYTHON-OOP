import random
from abc import ABCMeta,abstractmethod
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self,name,initialDeposit):
        return 0
    @abstractmethod
    def authenticate(self, name,accountNumber):
        return 0
    @abstractmethod
    def withdraw(self,withdrawalAmount):
        return 0
    @abstractmethod
    def deposit(self,depositAmount):
        return 0
    @abstractmethod
    def displayBalance(self):
        return 0
class Bank(Account):
    def __init__(self):
        self.customers={}
    def createAccount(self,name,initialDeposit):
        self.accountNumber=random.randint(10000,99999)
        self.customers[self.accountNumber]=[name,initialDeposit]
        print('Your account is:',self.accountNumber)
    def authenticate(self, name,accountNumber):
        if accountNumber in self.customers.keys():
            if self.customers[accountNumber][0]==name:
                print('Authentication is successful')
                self.accountNumber=accountNumber
                return True
            else:
                print('Authentication Failed')
                return False
        else:
            print('Authenticaton Failed')
    def withdraw(self,withdrawalAmount):
        if withdrawalAmount>self.customers[self.accountNumber][1]:
            print('Insufficient Balance')
        else:
            self.customers[self.accountNumber][1]-=withthdrawalAmount
            print('Withdrawal was successful',self.customers[self.accountNumber][1])
            self.displayBalance()
    def deposit(self,depositAmount):
        self.customers[self.accountNumber][1]+=depositAmount
        print('Deposit was sucessful')
        self.displayBalance()
    def displayBalance(self):
        print('Your Balance is:',self.customers[self.accountNumber][1])
cust=Bank()
while(True):
    print('Enter choice:')
    print('1. New Savings Account')
    print('2. Enter into Existing')
    print('3. Exit')
    ch=int(input())
    if(ch==1):
        print('Enter name and Initial deposit amount:')
        name,amount=input().split()
        initial=int(amount)
        cust.createAccount(name,initial)
        print('Your account details are:')
        cust.displayBalance()
    elif(ch==2):
        print('Enter you name and account number')
        name,acc=input().split()
        acc=int(acc)
        while(True):
            authStatus=cust.authenticate(name,acc)
            if authStatus is True:
                print('Enter 1. Withdraw')
                print('Enter 2. Deposit')
                print('Enter 3. Display Balance')
                print('Enter 4. Go Back')
                cho=int(input())
                if cho==1:
                    print('ENter withdrawal Amount')
                    withd=int(input())
                    cust.withdraw(withd)
                elif cho==2:
                    print('ENter deposited Amount')
                    dep=int(input())
                    cust.deposit(dep)
                elif cho==3:
                    cust.displayBalance()
                else:
                    break
    elif ch==3:
        exit()
