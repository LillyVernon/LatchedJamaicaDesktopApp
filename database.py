import mysql.connector
from datetime import date, datetime, timedelta


def connect():
    mydb = mysql.connector.connect(host= "localhost", user="root", passwd="", database="latchedjamaica")
    if(mydb):
        print("connection sucessful")
    else:
        print("connection unsuccesful")

    mycursor = mydb.cursor()
    #mycursor.execute("CREATE DATABASE LatchedJamaica")
    #mycursor.execute("Show databases")
    #for db in mycursor:
        #print(db)
    return  mydb, mycursor
#connect() 
      


def insertemployeeAccount(first_name, last_name, acctID, passwrd, username):
    mydb = mysql.connector.connect(host= "localhost", user="root", passwd="",database="latchjadb")
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addAccount = ("INSERT INTO account(firstname, lastname, accountID, password, username) VALUES (%s, %s, %s, %s, %s)")
    accountdata = (first_name, last_name, acctID, passwrd, username)
    mycursor.execute(addAccount, accountdata)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
    
def insertManagerAccount(first_name, last_name, acctID,managerID,passwrd, username):
    mydb = mysql.connector.connect(host= "localhost", user="root", passwd="",database="latchedjamaica")
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addAccount = ("INSERT INTO account(firstname, lastname, accountID, password, username) VALUES (%s, %s, %s, %s, %s)")
    accountdata = (first_name, last_name, acctID,passwrd, username)
    mycursor.execute(addAccount, accountdata)

    addManagerAccount = ("INSERT INTO managerAccount(firstname, lastname, accountID, managerAccountID, password, username) VALUES (%s, %s, %s, %s, %s, %s)")
    managerdata = (first_name, last_name, acctID, managerID,passwrd, username)
    mycursor.execute(addManagerAccount, managerdata)
    mydb.commit()
    mycursor.close()
    mydb.close()




def insertAlert(name,alertID,alertdate,itemID,itemCount):
    # alert date should a list of integer where [year, month, day] and do not use this
    # function if there's nothing in the inventory or items tables
    
    mydb = mysql.connector.connect(host= "localhost", user="root", passwd="",database="latchjadb")
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addAlert = ("INSERT INTO alert(name,alertID,alertdate,itemID,itemCount) VALUES (%s, %s, %s, %s, %s)")
    alertdata = (name,alertID,date(alertdate[0],alertdate[1],alertdate[2]),itemID,itemCount)
    mycursor.execute(addAlert, alertdata)
    mydb.commit()
    mycursor.close()
    mydb.close()







def buildTables():
    mydb = mysql.connector.connect(host= "localhost", user="root", passwd="",database="latchedjamaica")
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    tables = {}
    tables['account'] = ("Create table account(firstname varchar(30), lastname varchar(30), accountID varchar(30), password varchar(30), username varchar(30), primary key(accountID))")
    tables['managerAccount'] = ("Create table managerAccount(firstname varchar(30), lastname varchar(30), accountID varchar(30),managerAccountID varchar(30),password varchar(30), username varchar(30), primary key(ManagerAccountID), foreign key(accountID) references account(accountID)  on delete cascade)")
    tables['ordertable'] = ("Create table ordertable(name varchar(30), orderID varchar(30), totalprice FLOAT(50), discount FLOAT(50), accountID varchar(30),orderdate DATE, primary key(orderID),foreign key(accountID) references account(accountID)  on delete cascade)")
    tables['item'] = ("Create table item(itemname varchar(50), itemID varchar(30),itemprice float(50),itemcount int, itemdescription varchar(50), primary key(itemID))")
    tables['orderlist'] = ("Create table orderlist(orderID varchar(30), orderlistdate date,itemID varchar(30), primary key(orderID), foreign key(orderID) references ordertable(orderID)  on delete cascade,foreign key(itemID) references item(itemID)  on delete cascade)")
    tables['salary'] = ("Create table salary(salaryID varchar(30), accountID varchar(30),salaryAmount int, primary key(salaryID), foreign key(accountID) references account(accountID) on delete cascade)")
    tables['inventory'] = ("Create table inventory(inventoryID varchar(30), itemID varchar(30), quantity int, name varchar(30),primary key(inventoryID), foreign key(itemID) references item(itemID)  on delete cascade)")
    tables['alert'] = ("Create table alert(name varchar(30), alertID varchar(30),alertdate date, itemID varchar(30), itemCount int, primary key(alertID), foreign key(itemID) references item(itemID)  on delete cascade )")
    tables['supplier'] = ("Create table supplier(suppliername varchar(30), supplierID varchar(30),supplierlocation varchar(50), supplieritem varchar(30), itemID varchar(30), primary key(supplierID), foreign key(itemID) references item(itemID)  on delete cascade)")

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    mycursor.close()
    mydb.close()
#buildTables()
#nsertManagerAccount("ad", "min", 101,202,"root", "admin")
