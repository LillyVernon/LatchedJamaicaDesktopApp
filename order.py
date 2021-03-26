from tkinter import *
import tkinter as tk
import tkinter as tkk
import mysql.connector 
import tkinter.font as font
from functools import partial
from database import connect 


itemlist=[]
xitem=400
yitem=30
class Order(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #super(Order, self).__init__()
        self.geometry("700x500")
        self.configure(bg='pink')
        self.createorder()

    def additem(self):
        #return AdditemsGUI().mainloop()
        return self.displayitems()

    def createorder(self):
     
        self.myButton1 = tk.Button(self,text="Add Item",bg="#AEEEEE", width="20", command=self.additem)
        self.myButton1.place(y=30,x=20)

        self.myButton2 = tk.Button(self,text="Apply Discount",bg="#AEEEEE",width="20")
        self.myButton2.place(y=80,x=20)

        self.myButton3 = tk.Button(self,text="Delete Order",bg="#AEEEEE", width="20")
        self.myButton3.place(y=130,x=20)

        self.myButton4 = tk.Button(self,text="Check out",bg="#AEEEEE", width="20")
        self.myButton4.place(y=170,x=20)

        self.myButton5 = tk.Button(self, text="Sign out",bg="#f88379", width="20")
        self.myButton5.place(y=350,x=400)  

    def additemtoreceipt(self):
        global itemlist
        global xitem
        global yitem
        print("add item to list function")
        self.labelname = tk.Label(self, text=itemlist[-1][0])
        self.labelname.place(y=yitem,x=xitem)
        self.price=tk.Label(self, text=itemlist[-1][1]).place(y=yitem,x=xitem+60)
        self.count=tk.Label(self, text=itemlist[-1][3]).place(y=yitem,x=xitem+100)
        yitem=yitem+30
    

        #self.labelprice= tk.Label(self, text=price)
       # self.labelprice.place(y=yplace+100,x=xplace)

        #self.labelcount=tk.Label(self, text=num)  
        #self.labelcount.place(y=yplace+120,x=xplace)

#class AdditemsGUI(tkk.Tk):
    #def __init__(self, *args, **kwargs):
            #tk.Tk.__init__(self, *args, **kwargs)
           # self.geometry("600x400")
            #self.configure(bg='pink')
            #self.displayitems()

    def additems(self, name, iid):
        print(iid)
        info=(name,iid)
        con=connect()
        mycursor=connect()
        query = "SELECT itemname, itemprice FROM item where itemname = %s and itemID= %s "
        mycursor[1].execute(query, info,)
        myresult = mycursor[1].fetchall()
        print(myresult)
        return self.additemtoreceipt(myresult[0][0], myresult[0][1], 1, 30,50)


    def displayitems(self):
       # self.latched = tk.Label(self, text=" ",fg="black").pack()
        newwin = Toplevel(tk.Tk())
        newwin.title('Add items')
        newwin.geometry("600x400") 
        newwin.configure(bg='pink')

        newwin.resizable(0, 0)
        self.latched = Label(newwin, text="L a t c h e d  J a m a i c a",fg="black")
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
                addbutton = tkk.Button(newwin, text="+", width=5,height=1,bg="white",fg="black",  command=partial(self.addtoitemlist,self.x[0],self.x[2],self.x[4],1)) #command=lambda: self.additem(x[2])
                addbutton.place(y=self.starty,x=self.startx)

                self.itemname= tkk.Label(newwin,text=self.x[0])
                self.itemname.place(y=self.yy,x=self.xx)

                self.description= tkk.Label(newwin,text=self.x[4])
                self.description.place(y=self.yy+25,x=self.xx)

                self.itemcost= tkk.Label(newwin,text=self.x[2])
                self.itemcost.place(y=self.yy+50,x=self.xx)
                self.starty+=100
                self.yy+=100
            else: 
                self.addbutton = tkk.Button(newwin, text="+", width=5,height=1,bg="white",fg="black", command=partial(self.addtoitemlist,self.x[0],self.x[2],self.x[4],1))
                self.addbutton.place(y=self.startlefty,x=self.startleftx)

                self.itemname= tkk.Label(newwin,text=self.x[0])
                self.itemname.place(y=self.leftyy,x=self.leftxx)

                self.description= tkk.Label(newwin,text=self.x[4])
                self.description.place(y=self.leftyy+25,x=self.leftxx)

                self.itemcost= tkk.Label(newwin,text=self.x[2])
                self.itemcost.place(y=self.leftyy+50,x=self.leftxx)
                self.startlefty+=100
                self.leftyy+=100
        self.finish=tkk.Button(newwin, text="Finish Add Items", bg="white", fg="black", command=self.closeItemsWindow).place(y=self.leftyy+100,x=self.leftxx)

    def closeItemsWindow(self):
        self.totalprice=0
        for price in itemlist:
            print(price)
            self.totalprice+=price[1]
        return tk.Label(self, text="Total price is "+str(self.totalprice)).place(y=yitem,x=xitem)

    def getitems(self):
        con=connect()
        mycursor=connect()
        query="SELECT * from item"
        mycursor[1].execute(query)
        myresult = mycursor[1].fetchall()
        return myresult

    def addtoitemlist(self,name,desc, price,count):
        global itemlist
        print(itemlist)
        templist=[]
        templist.append(name)
        templist.append(desc)
        templist.append(price)
        templist.append(count)
        itemlist.append(tuple(templist))
        print(itemlist)
        
        return self.additemtoreceipt()
        
        #print(tuple(templist))

        

        
        # canvas = tk.Canvas(container, width=600, height=300)
        # canvas.grid(columnspan=3)

        # container.title("Latched Jamaica")
        # heading = tk.Label(container, text="Latched Jamaica", font="Raleway")
        # heading.grid(columnspan=3, column=0,row=10)

        # canvas = tk.Canvas(container, width=600, height=300)
        # canvas.grid(columnspan=3)
#o = Order()
#root.mainloop()

#def main():
    #root.configure(bg='pink')
#    app = Order()
#    app.mainloop()


#if __name__ == '__main__':
#    main()


