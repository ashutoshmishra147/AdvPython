"""
Bank Assignment

1.Add Account
2.Show Account
3.Withdraw
4.Deposit
5.Show All Accounts
6.Remove Account
7.Exit

"""

# AmountOverflowError
class AmountOverflowError(Exception):
    def __init__(self,errorMessage):
        self.errorMessage=errorMessage;

# InsufficeintBalanceError
class InsufficeintBalanceError(Exception):
    def __init__(self,errorMessage):
        self.errorMessage=errorMessage;



## define Account class
class Account:

    #constructor
    def __init__(self,accno,name,balance,accType="SV"):
        self.accno=accno;
        self.name=name;
        self.balance=balance;
        self.accType=accType;

    #function to show account details
    def showDetails(self):
        print("[Accno:",self.accno,"Name:",self.name,"Balance :",self.balance,"AccType :",self.accType,"]");

    #function to deposit money into account
    def deposit(self,amount):
        if(amount>50000):
            raise AmountOverflowError("You can deposit Maximum of Rs 50000/ only");
        self.balance=self.balance+amount;
        print("Account [",self.accno,"] is credited by Rs",amount,"/-");
        print("Total Balance in Account [",self.accno,"] is Rs",self.balance,"/-");

    #function to deposit money into account
    def withdraw(self,amount):
        if((self.balance-amount)<5000):
            raise InsufficeintBalanceError("You don't have sufficient balance in account");
        self.balance=self.balance-amount;
        print("Account [",self.accno,"] is debited by Rs",amount,"/-");
        print("Total Balance in Account [",self.accno,"] is Rs",self.balance,"/-");

    #function to get Accno 
    def getAccno(self):
        return self.accno;

    #function to get Name 
    def getName(self):
        return self.name;

    #function to get Balance
    def getBalance(self):
        return self.balance;


class Bank:
      def __init__(self):
          self.accountsMap={101:Account(101,"Amol Joshi",34000.4455),102:Account(102,"Pradeep Chinchole",45000.00),103:Account(103,"Prashant Mane",45000.00)};

      def addAccount(self,account):
          ##if account.accno in self.accountsMap
          ## raise Duplicate AccountNo
          
          self.accountsMap[account.getAccno()]=account;
          print("Account added successfully");

          
      def withdraw(self,accno,amount):
           if(accno in self.accountsMap):  
            self.accountsMap[accno].withdraw(amount);
           else:
            print("Accno [",accno,"] doesn't Exist");  

          
      def deposit(self,accno,amount):
          if(accno in self.accountsMap):  
            self.accountsMap[accno].deposit(amount);
          else:
            print("Accno [",accno,"] doesn't Exist");  

      def showAccount(self,accno):
          if(accno in self.accountsMap):  
            self.accountsMap[accno].showDetails();
          else:
            print("Accno [",accno,"] doesn't Exist");  

          
      def removeAccount(self,accno):
            if(accno in self.accountsMap):  
                del self.accountsMap[accno];
            else:
                print("Accno [",accno,"] doesn't Exist");  

      def showAllAccounts(self):
          print("Bank Accounts\n==================================");
          for accno in self.accountsMap:
              self.accountsMap[accno].showDetails();


choice=0;
#create bank object
bank=Bank();
while(choice<7):
    print("Banking Services");
    print("============================");
    print("1.Add Account");
    print("2.Show Account");
    print("3.Deposit Amount");
    print("4.Withdraw Amount");
    print("5.Show All Accounts");
    print("6.Remove Account");
    print("7.Exit")
    choice=int(input("Enter choice:"));
    if(choice==1):
        account=Account(int(input("Enter Accno:")),input("Enter Name:"),float(input("Enter Balance:")),input("Enter Account Type"));
        bank.addAccount(account);        
    elif(choice==2):
        bank.showAccount(int(input("Enter Accno")));
    elif(choice==3):
        bank.deposit(int(input("Enter Accno")),float(input("Enter Amount")));
    elif(choice==4):
        bank.withdraw(int(input("Enter Accno")),float(input("Enter Amount")));
    elif(choice==5):
        bank.showAllAccounts();
    elif(choice==6):
        bank.removeAccount(int(input("Enter Accno")));
           
 




          
          










    






    
    
        













        
    
