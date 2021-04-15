import tkinter as tk
import random
from tkinter import *
import tkinter.messagebox
import mysql.connector 
import tkinter.font as font
from datetime import date, datetime, timedelta
from calendar import day_name
from order import Order
from database import connect,generateReport,getAllItems,insertemployeeAccount, insertManagerAccount, salaryPayment, getSalary, getOrders  
LARGE_FONT= ("Verdana", 12)


class ManagerAccount(tk.Tk):
    def __init__(self,firstname,lastname, password, Username,accountid ,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.paySalary()
        self.displayManager()

    def OrderGUI(self):
        return Order(self.accountid).mainloop()

    def ViewPayments(self):
        return Salary(self.accountid).mainloop()

    def ViewALLorders(self):
        return OrderList(self.accountid).mainloop()

    def signOut(self):
        return self.destroy()


    def ViewReport(self):
        return Report().mainloop()


    def makeAccount(self):
        return NewAccount().mainloop()    

    def displayManager(self):
        label = tk.Label(self, text="Latched Jamaica", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        self.name= tk.Entry(self, fg="black", bg="white", width=40)
        self.name.pack(pady=8)
        self.namelabel = tk.Label(self, text="Manager Options")
        self.namelabel.pack()

        ##left hand side button
        self.createOrder = tk.Button(self,text="Create Order",
                                width=10,height=1,bg="white",fg="black"
                                ,command=self.OrderGUI)

        self.createOrder.place(y=150,x=100)

        self.viewSalary = tk.Button(self, text="View Salary",
                                    width=10,height=1,bg="white",fg="black", command = self.ViewPayments)
        self.viewSalary.place(y=200,x=100)

        self.viewreport = tk.Button(self, text="View Report",
                                    width=10,height=1,bg="white",fg="black", command = self.ViewReport)
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

        if day_name[thedate.weekday()] == 'Friday':
            salaryPayment()
            tkinter.messagebox.showinfo('LatchedJa : Salary Paid','Salary payments have been made. Click the View Salary option to see the payments')
            print('Today is Friday')

        else:
            
            tkinter.messagebox.showinfo('LatchedJa : Salary Warning','Salary payments can only be made on Fridays')    
            
            
class Salary(tk.Tk):
    def __init__(self, myaccountid,*args, **kwargs):
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
        



class OrderList(tk.Tk):
    def __init__(self, myaccountid,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.ViewOrderList()



    def ViewOrderList(self):
       
        mydata = getOrders()
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
            




class NewAccount(tk.Tk):
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







class Report(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.ViewReport()



    def ViewReport(self):
       
        myitemdata = getAllItems()
        myorderData = generateReport()
        data = []
        count = 0
        for x in myitemdata:
            data.append("ItemID: " + x[1]+" --Item Name: "+ x[0]+ " --Item Price: "+str(x[2]) +" --Quantity (in Stock): "+ str(x[3])+" --Item Description: "+x[4])
            count = count + 1
         



        self.tablelabel = tk.Label(self, text="Latched Jamaica Report")
        self.tablelabel.pack()
        
        # code for creating table
        #for i in range(total_rows):
        #    for j in range(total_columns):
                  
        #        self.e = tk.Entry(self, width=20, fg='blue',
        #                       font=('Arial',12,'bold'))
                  
        #        self.e.grid(row=i, column=j)
        #        self.e.insert(END, myorderData[i][j])



        self.data = tk.Text(self,height = 200, width = 500)
        self.data.pack()
        self.data.insert(tk.END, 'The Order Summary' + '\n'+'\n')

        for x in myorderData[0]:
            self.data.insert(tk.END, x + '\n')
            #self.data.insert(tk.END, myorderData[0][1])

        self.data.insert(tk.END, ' '+'\n')
        
        self.data.insert(tk.END, 'The Total Orders: '+ str(myorderData[2]) + '\n')
        self.data.insert(tk.END, 'The Total Revenue: '+ str(myorderData[1]) + '\n'+'\n')

        self.data.insert(tk.END, 'Inventory Summary'+'\n'+'\n')

        for x in data:
            self.data.insert(tk.END, x + '\n')

        self.data.insert(tk.END, ' '+'\n')
        self.data.insert(tk.END, 'The Total items: '+ str(count) + '\n') 
        self.data.configure(state='disabled')
        self.configure(bg='pink')
        self.geometry("1200x400")
        self.title("Latched Jamaica: Report")






#root = tk.Tk()
#root.geometry("600x400")
#root.configure(bg='pink')
#app = ManagerAccount()
#root.mainloop()

#start=ManagerAccount("nakeem","mcnally", "123", "nally","acc1202")
#start.geometry("600x400")
#start.mainloop()





        

    
        
 

#class Manager(Account):
