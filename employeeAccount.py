import tkinter as tk
from tkinter import *
import mysql.connector 
import tkinter.font as font
from order import Order
import database as dbmanager
LARGE_FONT= ("Verdana", 12)

class EmployeeAccount(tk.Tk):
    def __init__(self,firstname,lastname, password, Username,accountid, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.accountid = accountid
        self.displayManager()

    def OrderGUI(self):
        return Order(self.accountid).mainloop()
    
    def ViewPayments(self):
        return Salary(self.accountid).mainloop()

    def Viewmyorders(self):
        return OrderList(self.accountid).mainloop()
    
    def signOut(self):
        return self.destroy()


    def displayManager(self):
        label = tk.Label(self, text="Latched Jamaica", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        self.name= tk.Entry(self, fg="black", bg="white", width=40)
        self.name.pack(pady=8)
        self.namelabel = tk.Label(self, text="Employee Options")
        self.namelabel.pack()

        ##left hand side button
        self.createOrder = tk.Button(self,text="Create Order",
                                width=10,height=1,bg="white",fg="black"
                                ,command=self.OrderGUI)

        self.createOrder.place(y=150,x=100)

        self.viewSalary = tk.Button(self, text="View Salary",
                                    width=10,height=1,bg="white",fg="black",
                                    command = self.ViewPayments)
        self.viewSalary.place(y=200,x=100)

    

        ## right hand side buttons

        self.vieworder = tk.Button(self, text="View Orders",
                                    width=10,height=1,bg="white",fg="black",
                                   command=self.Viewmyorders)
        self.vieworder.place(y=150,x=400)



        self.signout = tk.Button(self, text="Sign Out",
                                    width=10,height=1,bg="white",fg="black",
                                 command=self.signOut)

        self.signout.place(y=350,x=500)
        
        self.geometry("600x400")
        self.configure(bg='pink')
        
        

class OrderList(tk.Tk):
    def __init__(self,myaccountid, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.myaccountid = myaccountid
        self.ViewOrderList()



    def ViewOrderList(self):
       
        mydata = dbmanager.getOrderByAccountID(self.myaccountid)
        mydata.insert(0,('Order ID','Cost', 'Discount', 'Account ID', 'Order Date'))
        total_rows = len(mydata)
        total_columns = len(mydata[0])
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = tk.Entry(self, width=20, fg='blue',
                               font=('Arial',12,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, mydata[i][j])


        
        
        self.configure(bg='pink')
        self.title("Latched Jamaica: View Orders")






            
class Salary(tk.Tk):
    def __init__(self,myaccountid, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.myaccountid = myaccountid
        self.ViewSalaryList()
        



    def ViewSalaryList(self):
       
        mydata = dbmanager.getSalaryByAccountID(self.myaccountid)
        mydata.insert(0,('SalaryID', 'AccountID','Amount Paid', 'Payment Date'))
        total_rows = len(mydata)
        total_columns = len(mydata[0])
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = tk.Entry(self, width=20, fg='blue',
                               font=('Arial',12,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, mydata[i][j])


        
        #self.geometry("600x600")
        self.configure(bg='pink')
        self.title("Latched Jamaica: View Salary")

#root = tk.Tk()
#root.geometry("600x400")
#root.configure(bg='pink')
#app = ManagerAccount()
#root.mainloop()

#start=Account()
#start.geometry("600x400")
#start.mainloop()
