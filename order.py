from tkinter import *
import tkinter as tk
import tkinter as tkk
import mysql.connector 
import tkinter.font as font
from functools import partial
from database import connect
from datetime import date, datetime, timedelta 
import tkinter.font as font


itemlist=[]
xitem=400
yitem=30
totalprice=0
accid=None
discount=0
#abelname=None
#price=None
#count=None
class Order(tk.Tk):
    def __init__(self, accountid, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        print("account id is " + str(accountid)) 
        global accid
        accid=accountid
        #super(Order, self).__init__()
        self.geometry("700x500")
        self.configure(bg='pink')
        self.createorder()

    def additem(self):
        #return AdditemsGUI().mainloop()
        return self.displayitems()

    def signOut(self):
        return self.destroy()
            

    def createorder(self):
     
        self.myButton1 = tk.Button(self,text="Add Item",bg="#AEEEEE", width="20", command=self.additem)
        self.myButton1.place(y=30,x=20)

        self.myButton2 = tk.Button(self,text="Apply Discount",bg="#AEEEEE",width="20", command=self.discount)
        self.myButton2.place(y=80,x=20)

        self.myButton3 = tk.Button(self,text="Delete Order",bg="#AEEEEE", width="20", command=self.deleteorder)
        self.myButton3.place(y=130,x=20)

        self.myButton4 = tk.Button(self,text="Check out",bg="#AEEEEE", width="20",command=self.checkout)
        self.myButton4.place(y=170,x=20)

        self.myButton5 = tk.Button(self, text="Sign out",bg="#f88379", width="20", command=self.signOut)
        self.myButton5.place(y=350,x=400)  

    def discount(self):
        global yitem
        self.labeldiscount = tk.Entry(self, fg="black", bg="white", width=10)
        self.labeldiscount.place(y=yitem,x=xitem)
        self.button = tk.Button(self,text="apply discount",width=14,height=1,bg="white",fg="black", command=self.applydiscount)
        self.button.place(y=yitem,x=xitem+70) 
        yitem+30

    def applydiscount(self):
        global itemlist
        global totalprice
        global discount
        discount=float(self.labeldiscount.get())
        print(discount)
        print(totalprice)
        totalprice=float(((100.0-discount)/100.0)*float(totalprice))
        print(totalprice)
        return totalprice
        

    def checkout(self):
        global accid
        global totalprice
        global itemlist
        global discount
        mycursor=connect()
        query = "SELECT orderID FROM orderlist ORDER BY orderID DESC LIMIT 1"
        mycursor[1].execute(query)
        myresult = list((mycursor[1].fetchall())[0])[0][5:]
        print(myresult)
        orderid="order" + str(int(myresult)+1)
        print(orderid)
        thedate =  datetime.today()
        addorder=("INSERT INTO ordertable(orderID, totalprice, discount, accountID, orderdate) VALUES (%s, %s, %s, %s, %s)")
        orderdata = (orderid, totalprice, discount, accid, thedate)
        mycursor[1].execute(addorder, orderdata,)
        
        for item in itemlist:
            addOrderlist = ("INSERT INTO orderlist(orderID, orderlistdate,itemname,orderedItemCount) VALUES (%s, %s, %s,%s)")
            orderlistdata = (orderid,thedate,item[1],item[5])
            mycursor[1].execute(addOrderlist, orderlistdata)
            mycursor[0].commit()
        tk.Label(self, text="Total Price after discount is " + str(totalprice) ).place(y=yitem+40,x=xitem)
        return tk.Label(self, text="ORDER COMPLETED").place(y=yitem+90,x=xitem)

    def additemtoreceipt(self):
        global itemlist
        global xitem
        global yitem
        itemlist[-1].append(yitem)
        print("add item to list function")
        labelname = tk.Label(self, text=itemlist[-1][1])
        labelname.place(y=yitem,x=xitem)
        self.price=tk.Label(self, text=itemlist[-1][3]).place(y=yitem,x=xitem+60)
        count=tk.Label(self, text=itemlist[-1][5]).place(y=yitem,x=xitem+120)
        yitem=yitem+30
        
    def deleteorder(self):
        self.destroy()
        global itemlist
        global xitem
        global yitem
        xitem=400
        yitem=30
        itemlist.clear()
        Order()


    def additems(self, name, iid):
        print(iid)
        info=(name,iid)
        con=connect()
        mycursor=connect()
        query = "SELECT itemname, itemID, itemprice FROM item where itemname = %s and itemID= %s "
        mycursor[1].execute(query, info,)
        myresult = list(mycursor[1].fetchall())
        print("my result is")
        print(myresult)
        return self.additemtoreceipt(myresult[0][0], myresult[0][1],myresult[0][2], 1, 30,50)


    def displayitems(self):
       # self.latched = tk.Label(self, text=" ",fg="black").pack()
        self.newwin = Toplevel(Tk())
        self.newwin.title('Add items')
        self.newwin.geometry("600x400") 
        self.newwin.configure(bg='pink')

        self.newwin.resizable(0, 0)
        self.latched = Label(self.newwin, text="L a t c h e d  J a m a i c a",fg="black")
        self.latched.pack()
        self.item=self.getitems()
        self.startx=20
        self.starty=30
        self.xx=70
        self.yy=20
        self.startleftx=300
        self.startlefty=30
        self.leftxx=350
        self.leftyy=30

        for self.x in self.item:
            
            if self.item.index(self.x)%2==0:
                addbutton = tkk.Button(self.newwin, text="+", width=5,height=1,bg="white",fg="black",  command=partial(self.addtoitemlist,self.x[0],self.x[1],self.x[2],self.x[4],1)) #command=lambda: self.additem(x[2])
                addbutton.place(y=self.starty,x=self.startx)

                self.itemname= tkk.Label(self.newwin,text=self.x[0])
                self.itemname.place(y=self.yy,x=self.xx)

                self.description= tkk.Label(self.newwin,text=self.x[4])
                self.description.place(y=self.yy+25,x=self.xx)

                self.itemcost= tkk.Label(self.newwin,text=self.x[2])
                self.itemcost.place(y=self.yy+50,x=self.xx)
                self.starty+=100
                self.yy+=100
            else: 
                self.addbutton = tkk.Button(self.newwin, text="+", width=5,height=1,bg="white",fg="black", command=partial(self.addtoitemlist,self.x[0],self.x[1],self.x[2],self.x[4],1))
                self.addbutton.place(y=self.startlefty,x=self.startleftx)

                self.itemname= tkk.Label(self.newwin,text=self.x[0])
                self.itemname.place(y=self.leftyy,x=self.leftxx)

                self.description= tkk.Label(self.newwin,text=self.x[4])
                self.description.place(y=self.leftyy+25,x=self.leftxx)

                self.itemcost= tkk.Label(self.newwin,text=self.x[2])
                self.itemcost.place(y=self.leftyy+50,x=self.leftxx)
                self.startlefty+=100
                self.leftyy+=100
        self.finish=tkk.Button(self.newwin, text="Finish Add Items", bg="white", fg="black", command=self.closeItemsWindow).place(y=self.leftyy+100,x=self.leftxx)

    def closeItemsWindow(self):
        global totalprice
        global yitem
        #self.totalprice=0
        for price in itemlist:
            print(price)
            totalprice+=price[4]
        tk.Label(self, text="SUB TOTAL IS "+str(totalprice)).place(y=yitem,x=xitem)
        yitem=yitem+30
        return self.newwin.destroy()

    def getitems(self):
        con=connect()
        mycursor=connect()
        query="SELECT * from item"
        mycursor[1].execute(query)
        myresult = mycursor[1].fetchall()
        return myresult

    def addtoitemlist(self,name,iid, price,desc,count):
        global itemlist
        global xitem
        global yitem
        print(itemlist)
        templist=[]
        check=(any(iid in sl for sl in itemlist))
        print(check)
        if check==True:
            print("item in list")
            for item in itemlist:
                print(item)
                if int(item[0])==int(iid):
                    item[5]=item[5]+1
                    pri=item[3]
                    item[4]=pri*item[5]
                    tk.Label(self, text=item[5]).place(y=item[-1],x=xitem+120)
                    tk.Label(self, text=item[4]).place(y=item[-1],x=xitem+60)
                    break

        else:
            print("new item")
            templist.append(iid)
            templist.append(name)
            templist.append(desc)
            templist.append(price)
            templist.append(price)
            templist.append(count)
            itemlist.append(templist)
            print(itemlist)
            return self.additemtoreceipt()
    
