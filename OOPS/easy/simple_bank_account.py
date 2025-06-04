# Design a BankAccount class with the following functionality:
# Attributes: account_holder (string), balance (float, default 0.0)

# Methods:
# deposit(amount) – adds to balance
# withdraw(amount) – subtracts from balance if sufficient funds
# display_balance() – prints current balance

# Constraints:
# Prevent overdrawing by checking the balance before withdrawal. Raise an exception or print a warning if funds are insufficient.

# postgresql://neondb_owner:npg_mRSDIQHw70yd@ep-winter-firefly-a1gpf208-pooler.ap-southeast-1.aws.neon.tech/bank?sslmode=require
import psycopg2
# connection_string="postgresql://neondb_owner:npg_mRSDIQHw70yd@ep-winter-firefly-a1gpf208-pooler.ap-southeast-1.aws.neon.tech/bank?sslmode=require"
# # Connect to the School database
# conn = psycopg2.connect(connection_string)

# def connection():
#     base_connection=conn.cursor()
#     print("connection established")
#     base_connection.execute("CREATE TABLE Persons (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));")
#     print("table created")
#     base_connection.close()
    
# connection()
def connect_with_string():
    # Your Neon connection string format:
    # postgresql://username:password@hostname:port/database?sslmode=require
    connection_string = "postgresql://neondb_owner:npg_mRSDIQHw70yd@ep-winter-firefly-a1gpf208-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

    try:
        conn = psycopg2.connect(connection_string)
        print("Connected successfully!")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None


db = connect_with_string()
def createTable():
    db.cursor().execute(
        """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_active BOOLEAN DEFAULT TRUE
    );"""
    )
    db.commit()
    print("Table created successfully!")


createTable()
 

 

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
   
   
    