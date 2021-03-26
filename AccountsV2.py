import tkinter as tk
import random
from tkinter import *
import tkinter.messagebox
import mysql.connector 
import tkinter.font as font
from datetime import date, datetime, timedelta
from calendar import day_name
from orderV2 import Order
from database import connect, insertemployeeAccount, insertManagerAccount, salaryPayment, getSalary, getOrders  
LARGE_FONT= ("Verdana", 12)

class ManagerAccount(tk.Tk):
    def __init__(self,firstname,lastname, password, Username,accountid ,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.paySalary()
        self.displayManager()

    def OrderGUI(self):
        self.destroy()
        return Order()

    def ViewPayments(self):
        return ViewSalaryPaid().mainloop()

    def ViewALLorders(self):
        return ViewAllOrdersMade().mainloop()

    def signOut(self):
        return self.destroy()

    def makeAccount(self):
        return CreateNewAccount().mainloop()    

    def displayManager(self):
        label = tk.Label(self, text="Latched Jamaica", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        self.name= tk.Entry(self, fg="black", bg="white", width=40)
        self.name.pack(pady=8)
        self.namelabel = tk.Label(self, text="Manager Options")
        self.namelabel.pack()

        ##left hand side button
        self.createOrder = tk.Button(self,text="Creat Order",
                                width=10,height=1,bg="white",fg="black"
                                ,command=self.OrderGUI)

        self.createOrder.place(y=150,x=100)

        self.viewSalary = tk.Button(self, text="View Salary",
                                    width=10,height=1,bg="white",fg="black", command = self.ViewPayments)
        self.viewSalary.place(y=200,x=100)

        self.viewreport = tk.Button(self, text="View Report",
                                    width=10,height=1,bg="white",fg="black")
        self.viewreport.place(y=250,x=100)


        self.updateitem = tk.Button(self, text="Update Item",
                                    width=10,height=1,bg="white",fg="black")
        self.updateitem.place(y=300,x=100)

        ## right hand side buttons

        self.vieworder = tk.Button(self, text="View Orders",
                                    width=10,height=1,bg="white",fg="black", command = self.ViewALLorders)
        self.vieworder.place(y=150,x=400)

        self.createAccount = tk.Button(self, text="Create User",
                            width=10,height=1,bg="white",fg="black",
                                       command = self.makeAccount)
        self.createAccount.place(y=200,x=400)


        self.addNewItem = tk.Button(self, text="Add New Item",
                                    width=10,height=1,bg="white",fg="black")
        self.addNewItem.place(y=250,x=400)

        self.paySalarybtn = tk.Button(self, text="Pay Salary",
                                    width=10,height=1,bg="white",fg="black", command = self.paySalary)
        self.paySalarybtn.place(y=300,x=400)

        self.signout = tk.Button(self, text="Sign Out",
                                    width=10,height=1,bg="white",fg="black",
                                 command=self.signOut)
        self.signout.place(y=350,x=500)
        
        self.geometry("600x400")
        self.configure(bg='pink')



    def paySalary(self):
        thedate =  datetime.today()

        if day_name[thedate.weekday()] == 'Wednesday':
            salaryPayment()
            tkinter.messagebox.showinfo('LatchedJa : Salary Paid','Salary payments have been made. Click the View Salary option to see the payments')
            print('Today is Friday')

        else:
            
            tkinter.messagebox.showinfo('LatchedJa : Salary Warning','Salary payments can only be made on Fridays')    
            
            
class ViewSalaryPaid(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.ViewSalaryList()



    def ViewSalaryList(self):
       
        mydata = getSalary()
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
        



class ViewAllOrdersMade(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.ViewOrderList()



    def ViewOrderList(self):
       
        mydata = getOrders()
        mydata.insert(0,('Order Name', 'Order ID','Cost', 'Discount', 'Account ID', 'Order Date'))
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
            




class CreateNewAccount(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.CreateAddaccount()


    def makeUser(self):
        self.newfirstname = self.firstname.get()
        self.newlastname = self.lastname.get()
        self.newpassword = self.password.get()
        self.newusername = self.name.get()
        self.selection = self.select.get()
        
        if(self.selection == 'M'):
            print('you selected '+ self.selection)
            c = str(random.randint(1000,2000))
            idcode = 'manacc' + c
            print(idcode)
            idcode2 = 'acc' + c +'-M'    
            insertManagerAccount(self.newfirstname, self.newlastname,
                                 idcode2,idcode,self.newpassword, self.newusername)


        if(self.selection == 'E'):
            print('you selected '+ self.selection)
            idcode = 'acc' + str(random.randint(1000,2000))
            insertemployeeAccount(self.newfirstname,self.newlastname, idcode,
                              self.newpassword,self.newusername)

        return self.destroy()


    def CreateAddaccount(self):
        
        label = tk.Label(self, text="Latched Jamaica", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.firstnamelabel = tk.Label(self, text="First Name")
        self.firstnamelabel.pack()
        self.firstname= tk.Entry(self, fg="black", bg="white", width=40)
        self.firstname.pack(pady=8)
        

        self.lastnamelabel = tk.Label(self, text="Last Name")
        self.lastnamelabel.pack()
        self.lastname= tk.Entry(self, fg="black", bg="white", width=40)
        self.lastname.pack(pady=8)

        self.namelabel = tk.Label(self, text="Username")
        self.namelabel.pack()
        self.name= tk.Entry(self, fg="black", bg="white", width=40)
        self.name.pack(pady=8)
       
        
        self.passwordlabel = tk.Label(self,text="Password")
        self.password= tk.Entry(self,fg="black", bg="white", width=40, show='*')
        self.passwordlabel.pack()
        self.password.pack(pady=8)

        #self.var = tk.StringVar()

        #self.select = tk.Label(self, text="Select Account type")
        #self.select.pack()

        #self.manageroption = tk.Radiobutton(self, text="Manager Account", variable=self.var, value='M')
        #self.manageroption.pack(pady=8)

        #self.employeeoption = tk.Radiobutton(self, text="Employee Account", variable=self.var, value='E')
        #self.employeeoption.pack(pady=8)

        self.selecttype = tk.Label(self, text="Enter 'M' for manager account or 'E' for employee account")
        self.selecttype.pack()
        self.select = tk.Entry(self, fg="black", bg="white", width=40)
        self.select.pack(pady=8)

        self.button = tk.Button(self,text="Create Account",width=11,height=1,bg="white",
                                fg="black",command= self.makeUser)
        self.button.pack(pady=8)

        self.geometry("600x450")
        self.configure(bg='pink')




#root = tk.Tk()
#root.geometry("600x400")
#root.configure(bg='pink')
#app = ManagerAccount()
#root.mainloop()

#start=ManagerAccount("nakeem","mcnally", "123", "nally","acc1202")
#start.geometry("600x400")
#start.mainloop()






class Account:
    
    def __init__(self, firstname,lastname, password, Username):
        self.firstname = firstname
        self.lastname = lasttname
        self.password = password
        self.Username = Username
        self.salary = 0
        self.AccountID = 0

    def displayuser(self):
        return self.Username
        

    
        
 

#class Manager(Account):
