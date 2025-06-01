# Design a BankAccount class with the following functionality:
# Attributes: account_holder (string), balance (float, default 0.0)

# Methods:
# deposit(amount) – adds to balance
# withdraw(amount) – subtracts from balance if sufficient funds
# display_balance() – prints current balance

# Constraints:
# Prevent overdrawing by checking the balance before withdrawal. Raise an exception or print a warning if funds are insufficient.


class BankAccount():
    def __init__(self,account_holder: str, balance: float=0.0):
        self.account_holder=account_holder
        self.balance=balance
        pass
    
    
    def deposit(self,amount:float):
        self.balance +=amount
        return self.balance
    def withdraw(self,amount:float):
        if(amount>self.balance):
            return 'insufficent balance'
        else:    
            self.balance -=amount
            return self.balance
        # self.amount=self.balance - amount
        # return f"{self.amount}" ///this stores value in amount but we need to store it in balance so that final balance gets updated
    def display_balance(self):
        return f"{self.balance}"
    

name=input("enter acount_holder name: ")
balance=float(input("enter your initial balance: "))    
acct_details=BankAccount(name,balance) 



while True:
    service=input("what whould you like to do?\na. Withdraw\nb. deposite\nc. check balnce:\nd. exit \n")
    if(service=='a'):
        amount=float(input("enter the amount you want to withdraw: "))
        withdraw_amount=acct_details.withdraw(amount)
        print(withdraw_amount)
    elif(service=='b'):
        amount=float(input("enter the amount you want to deposit: "))
        deposite_amount=acct_details.deposit(amount)
        print(deposite_amount)  
    elif(service=='c'):
        balance_amount=acct_details.display_balance()   
        print(balance_amount) 
    elif(service=='d'):
        break
    else:
        print('select the correct option')    
    
      
  
# print(acct_details.deposit(122.0)) 
# print(acct_details.withdraw(122.0))
# print(acct_details.display_balance())
   
    