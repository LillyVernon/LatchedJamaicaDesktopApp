import tkinter as tk
import mysql.connector 
import tkinter.font as font
from order import Order
LARGE_FONT= ("Verdana", 12)

class Account(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.displayManager()

    def OrderGUI(self):
        self.destroy()
        return Order().mainloop()


    def signOut(self):
        return self.destroy()


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

    

        ## right hand side buttons

        self.vieworder = tk.Button(self, text="View Orders",
                                    width=10,height=1,bg="white",fg="black")
        self.vieworder.place(y=150,x=400)



        self.signout = tk.Button(self, text="Sign Out",
                                    width=10,height=1,bg="white",fg="black",
                                 command=self.signOut)

        self.signout.place(y=350,x=500)
        
        self.geometry("600x400")
        self.configure(bg='pink')
        
        






#root = tk.Tk()
#root.geometry("600x400")
#root.configure(bg='pink')
#app = ManagerAccount()
#root.mainloop()

start=Account()
start.geometry("600x400")
start.mainloop()
