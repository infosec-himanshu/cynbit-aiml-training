class BankAccount:
    def __init__(self,account_number,balance):
        print("hello good morning")
        self.account_number=account_number
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("Diposited:",amount)
        
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdraw",amount)
        else:
            print("insufficient balance")
        
    def display(self):
        print("Account Number:",self.account_number)
        print("Balance:",self.balance)
    

acc=BankAccount(1111,50000)
acc.deposit(2000)
acc.withdraw(7000)
acc.display()
print("\n")
ac=BankAccount(1112,50000)
ac.deposit(2000)
ac.withdraw(500)
ac.display()
