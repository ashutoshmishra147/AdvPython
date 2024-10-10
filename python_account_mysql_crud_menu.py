"""
Application to perform CRUD Operation
on account table in bank databse of MySQL;
"""
import mysql.connector

db= mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='bank');






# prepare a cursor object using cursor() method
cursor = db.cursor()

# dispaly all records from account
def showAllAccounts():
    cursor.execute("SELECT * FROM ACCOUNT");
    data=cursor.fetchall();
    print("Updated Bank Accounts\n====================================")
    for row in data:
        print(row);
# add account
def addAccount(accno,name,balance):
    cursor.execute("INSERT INTO ACCOUNT VALUES('%d','%s','%d')"%(accno,name,balance));
    db.commit();
    print("Account added successfully");

# remove account
def removeAccount(accno):
    cursor.execute("DELETE FROM ACCOUNT WHERE ACCNO='%d'"%(accno));
    db.commit();    
    print("Account delete successfully");

#withdraw
def withdraw(accno,amount):
    cursor.execute("UPDATE ACCOUNT SET BALANCE=BALANCE-'%d' WHERE ACCNO='%d'"%(amount,accno));
    db.commit();    
    print("Account [",accno,"] is debited by Rs ",amount,"/-");

# deposit
def deposit(accno,amount):
    cursor.execute("UPDATE ACCOUNT SET BALANCE=BALANCE+'%d' WHERE ACCNO='%d'"%(amount,accno));
    db.commit();    
    print("Account [",accno,"] is credited by Rs ",amount,"/-");


#show Account    
def showAccount(accno):
    cursor.execute("SELECT * FROM ACCOUNT WHERE ACCNO='%d'"%(accno));
    data=cursor.fetchone(); 
    print("Account Details :",data);



choice=0;
#create bank object
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
        addAccount(int(input("Enter Accno:")),input("Enter Name:"),float(input("Enter Balance:")));
    elif(choice==2):
        showAccount(int(input("Enter Accno")));
    elif(choice==3):
        deposit(int(input("Enter Accno")),float(input("Enter Amount")));
    elif(choice==4):
        withdraw(int(input("Enter Accno")),float(input("Enter Amount")));
    elif(choice==5):
        showAllAccounts();
    elif(choice==6):
        removeAccount(int(input("Enter Accno")));
           


# disconnect from server
db.close()

















