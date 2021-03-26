import tkinter as tk
import mysql.connector 
import tkinter.font as font
from database import connect 

class AdditemsGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.geometry("600x400")
            self.configure(bg='pink')
            self.displayitems()

    def displayitems(self):
       # self.latched = tk.Label(self, text=" ",fg="black").pack()
        self.latched = tk.Label(self, text="L a t c h e d  J a m a i c a",fg="black")
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

        for x in self.item:
            if self.item.index(x)%2==0:
                self.addbutton = tk.Button(self, text="+", width=5,height=1,bg="white",fg="black")
                self.addbutton.place(y=self.starty,x=self.startx)

                self.itemname= tk.Label(self,text=x[0])
                self.itemname.place(y=self.yy,x=self.xx)

                self.description= tk.Label(self,text=x[4])
                self.description.place(y=self.yy+25,x=self.xx)

                self.itemcost= tk.Label(self,text=x[2])
                self.itemcost.place(y=self.yy+50,x=self.xx)
                self.starty+=100
                self.yy+=100
            else: 
                self.addbutton = tk.Button(self, text="+", width=5,height=1,bg="white",fg="black")
                self.addbutton.place(y=self.startlefty,x=self.startleftx)

                self.itemname= tk.Label(self,text=x[0])
                self.itemname.place(y=self.leftyy,x=self.leftxx)

                self.description= tk.Label(self,text=x[4])
                self.description.place(y=self.leftyy+25,x=self.leftxx)

                self.itemcost= tk.Label(self,text=x[2])
                self.itemcost.place(y=self.leftyy+50,x=self.leftxx)
                self.startlefty+=100
                self.leftyy+=100

            
    def getitems(self):
        con=connect()
        mycursor=connect()
        query="SELECT * from item"
        mycursor[1].execute(query)
        myresult = mycursor[1].fetchall()
        #print(myresult)
        #for x in myresult:
           # print (x)
        return myresult
 



#a=AdditemsGUI()
#a.mainloop()