import mysql.connector
import random
from datetime import date, datetime, timedelta



#database information

hostName = "localhost"
databaseUser = "root"
databasePassword = ""
databaseName = "latchjadb"


# latchja info

FlatSalaryRate = 25000

def connect():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
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
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
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
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
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




def insertAlert(name,alertID,itemID,itemCount):
    thedate =  datetime.today()
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addAlert = ("INSERT INTO alert(name,alertID,alertdate,itemID,itemCount) VALUES (%s, %s, %s, %s, %s)")
    alertdata = (name,alertID,thedate,itemID,itemCount)
    mycursor.execute(addAlert, alertdata)
    mydb.commit()
    mycursor.close()
    mydb.close()

def getAllAlerts():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM alert")
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)
    mydb.commit()
    mycursor.close()
    mydb.close()

def insertSalary(salaryID, accountID, salaryAmount):
    thedate =  datetime.today()
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addSalary = ("INSERT INTO salary(salaryID,accountID,salaryAmount,salaryDate) VALUES (%s, %s, %s, %s)")
    salarydata = (salaryID,accountID,salaryAmount,thedate)
    mycursor.execute(addSalary, salarydata)
    mydb.commit()
    mycursor.close()
    mydb.close()
    

def getSalaryByAccountID(accountID):
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM salary WHERE accountID = %s")
    mycursor.execute(query, (accountID,))
    myresult = mycursor.fetchall()
    print(myresult)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return myresult
    
def getSalary():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM salary")
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return myresult

def getItemByName(itemName):
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM item WHERE itemname = %s")
    mycursor.execute(query, (itemName,))
    myresult = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return myresult

    
def getAllItems():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM item")
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(myresult)
    mydb.commit()
    mycursor.close()
    mydb.close()


def deleteItemByName(itemName):
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("DELETE FROM item WHERE itemname = %s")
    mycursor.execute(query, (itemName,))
    mydb.commit()
    mycursor.close()
    mydb.close()
   


def insertItem(itemname, itemID,itemprice,itemcount, itemdescription):

    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addItem = ("INSERT INTO item(itemname, itemID,itemprice,itemcount, itemdescription) VALUES (%s, %s, %s, %s, %s)")
    itemdata = (itemname, itemID,itemprice,itemcount, itemdescription)
    mycursor.execute(addItem, itemdata)
    mydb.commit()
    mycursor.close()
    mydb.close()




def updateItemByName(oldname, newitemname, newitemID,newitemprice,newitemcount, newitemdescription):
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addItem = ("UPDATE item SET itemname = %s, itemID = %s,itemprice = %s ,itemcount = %s, itemdescription = %s WHERE itemname = %s")
    itemdata = (newitemname, newitemID,newitemprice,newitemcount, newitemdescription, oldname)
    mycursor.execute(addItem, itemdata)
    mydb.commit()
    mycursor.close()
    mydb.close()




def updateItemPriceByName(itemname, newitemprice):

    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addItem = ("UPDATE item SET itemprice = %s WHERE itemname = %s")
    itemdata = (newitemprice, itemname)
    mycursor.execute(addItem, itemdata)
    mydb.commit()
    mycursor.close()
    mydb.close()
    

def updateItemCountByName(itemname, newitemcount):

    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addItem = ("UPDATE item SET itemcount = %s WHERE itemname = %s")
    itemdata = (newitemcount, itemname)
    mycursor.execute(addItem, itemdata)
    mydb.commit()
    mycursor.close()
    mydb.close()


def reduceItemCountByName(itemname, reductionAmount):
    #this is used when an item is ordered and a specific quantity is requested
    # so the itemcount should be reduced by that value in order to update the inventory

    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT itemcount FROM item WHERE itemname = %s")
    mycursor.execute(query,(itemname,))
    myresult = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    updateItemCountByName(itemname,myresult[0][0]-reductionAmount)
    
   
def insertOrder(name, orderID, totalprice, discount, accountID, itemname, orderedItemCount):
    thedate =  datetime.today()
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    addOrder = ("INSERT INTO ordertable(name, orderID, totalprice, discount, accountID, orderdate) VALUES (%s, %s, %s, %s, %s, %s)")
    orderdata = (name, orderID, totalprice, discount, accountID, thedate)
    mycursor.execute(addOrder, orderdata)

    addOrderlist = ("INSERT INTO orderlist(orderID, orderlistdate,itemname,orderedItemCount) VALUES (%s, %s, %s,%s)")
    orderlistdata = (orderID,thedate,itemname,orderedItemCount)
    mycursor.execute(addOrderlist, orderlistdata)
    
    mydb.commit()
    mycursor.close()
    mydb.close()
    reduceItemCountByName(itemname, orderedItemCount)
    
#insertOrder('Ms Davis','order1564',750,0,'acc1001','high class watch',4)


def getOrders():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM ordertable")
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return myresult


def getOrderByAccountID(accountID):
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT * FROM ordertable WHERE accountID = %s")
    mycursor.execute(query, (accountID,))
    myresult = mycursor.fetchall()
    print(myresult)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return myresult




def salaryPayment():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    query = ("SELECT accountID FROM account")
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    todaysdate = datetime.today()
    
    days = timedelta(5)
    limitdate = todaysdate - days
   
    for x in myresult:
        print(x[0])
        query = ("SELECT orderID FROM ordertable WHERE accountID = %s and orderdate > %s")
        mycursor.execute(query,(x[0],limitdate,))
        data = mycursor.fetchall()
        salesMade = len(data) * 500
        pay = salesMade + FlatSalaryRate
        #pay salary
        salaryID = 'salary' + str(random.randint(1000,2000))
        insertSalary(salaryID, x[0], pay)
        

    mydb.commit()
    mycursor.close()
    mydb.close()
    
    
    
    
    




def buildTables():
    mydb = mysql.connector.connect(host= hostName, user=databaseUser, passwd=databasePassword, database=databaseName)
    if(mydb):
        print("connection made")

    mycursor = mydb.cursor()
    tables = {}
    tables['account'] = ("Create table account(firstname varchar(30), lastname varchar(30), accountID varchar(30), password varchar(30), username varchar(30), primary key(accountID))")
    tables['managerAccount'] = ("Create table managerAccount(firstname varchar(30), lastname varchar(30), accountID varchar(30),managerAccountID varchar(30),password varchar(30), username varchar(30), primary key(ManagerAccountID), foreign key(accountID) references account(accountID)  on delete cascade)")
    tables['ordertable'] = ("Create table ordertable(name varchar(30), orderID varchar(30), totalprice FLOAT(50), discount FLOAT(50), accountID varchar(30),orderdate DATE, primary key(orderID),foreign key(accountID) references account(accountID)  on delete cascade)")
    tables['item'] = ("Create table item(itemname varchar(50), itemID varchar(30),itemprice float(50),itemcount int, itemdescription varchar(50), primary key(itemID))")
    tables['orderlist'] = ("Create table orderlist(orderID varchar(30), orderlistdate date,itemname varchar(50),orderedItemCount int, primary key(orderID), foreign key(orderID) references ordertable(orderID)  on delete cascade)")
    tables['salary'] = ("Create table salary(salaryID varchar(30), accountID varchar(30),salaryAmount int,salaryDate DATE, primary key(salaryID), foreign key(accountID) references account(accountID) on delete cascade)")
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

