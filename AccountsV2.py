import tkinter as tk
import mysql.connector 
import tkinter.font as font
from order import Order
from database import connect
LARGE_FONT= ("Verdana", 12)

class ManagerAccount(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.displayManager()

    def OrderGUI(self):
        self.destroy()
        return Order().mainloop()


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
                                    width=10,height=1,bg="white",fg="black")
        self.viewSalary.place(y=200,x=100)

        self.viewreport = tk.Button(self, text="View Report",
                                    width=10,height=1,bg="white",fg="black")
        self.viewreport.place(y=250,x=100)


        self.updateitem = tk.Button(self, text="Update Item",
                                    width=10,height=1,bg="white",fg="black")
        self.updateitem.place(y=300,x=100)

        ## right hand side buttons

        self.vieworder = tk.Button(self, text="View Orders",
                                    width=10,height=1,bg="white",fg="black")
        self.vieworder.place(y=150,x=400)

        self.createAccount = tk.Button(self, text="Create User",
                            width=10,height=1,bg="white",fg="black",
                                       command = self.makeAccount)
        self.createAccount.place(y=200,x=400)


        self.addNewItem = tk.Button(self, text="Add New Item",
                                    width=10,height=1,bg="white",fg="black")
        self.addNewItem.place(y=250,x=400)

        self.signout = tk.Button(self, text="Sign Out",
                                    width=10,height=1,bg="white",fg="black",
                                 command=self.signOut)
        self.signout.place(y=350,x=500)
        
        self.geometry("600x400")
        self.configure(bg='pink')
        
        




class CreateNewAccount(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.CreateAddaccount()



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


        self.button = tk.Button(self,text="Create Account",width=11,height=1,bg="white",
                                fg="black")
        self.button.pack(pady=8)

        self.geometry("600x400")
        self.configure(bg='pink')




#root = tk.Tk()
#root.geometry("600x400")
#root.configure(bg='pink')
#app = ManagerAccount()
#root.mainloop()

#start=ManagerAccount()
#start.geometry("600x400")
#start.mainloop()
