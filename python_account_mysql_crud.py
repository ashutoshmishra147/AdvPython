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

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s "%data);

# add 5 records to account

cursor.execute("INSERT INTO ACCOUNT VALUES(101,'PRADEEP',12000.00)");
cursor.execute("INSERT INTO ACCOUNT VALUES(102,'PRATAP',13000.00)");
cursor.execute("INSERT INTO ACCOUNT VALUES(103,'PRAKASH',14000.00)");
cursor.execute("INSERT INTO ACCOUNT VALUES(104,'PRAMOD',15000.00)");
cursor.execute("INSERT INTO ACCOUNT VALUES(105,'PRANAL',16000.00)");

print("5 records inserted.....")
db.commit();

# display all records from account
cursor.execute("SELECT * FROM ACCOUNT");
data=cursor.fetchall();

print("BAnk Accounts\n====================================")
for row in data:
    print(row);

# delete accounts whose balance is <14000

cursor.execute("DELETE FROM ACCOUNT WHERE BALANCE<14000");

# update the balance of all accounts by 5%

cursor.execute("UPDATE ACCOUNT SET BALANCE=BALANCE+0.05*BALANCE");

db.commit();

# dispaly all records from account

cursor.execute("SELECT * FROM ACCOUNT");
data=cursor.fetchall();

print("Updated Bank Accounts\n====================================")
for row in data:
    print(row);

# disconnect from server
db.close()


