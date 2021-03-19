import tkinter as tk
import mysql.connector 
import tkinter.font as font
from database import connect 
from AccountsV2 import ManagerAccount
from employeeAccount import Account

LARGE_FONT= ("Verdana", 12)


class LoginPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.displaylogin()


    def displaylogin(self):
        
        label = tk.Label(self, text="Latched Jamaica", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.namelabel = tk.Label(self, text="Name")
        self.namelabel.pack()
        self.name= tk.Entry(self, fg="black", bg="white", width=40)
        self.name.pack(pady=8)
       

        self.passwordlabel = tk.Label(self,text="Password")
        self.password= tk.Entry(self,fg="black", bg="white", width=40, show='*')
        self.passwordlabel.pack()
        self.password.pack(pady=8)
        #widget.pack_forget()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.entry.pack_forget()

        self.button = tk.Button(self,
        text="Login",
        width=10,
        height=1,
        bg="white",
        fg="black",
        command=self.submit
         )
        self.button.pack(pady=8)  

    def login(self, username,userpassword):
        if self.userpassword and self.username:
            print(self.userpassword)
            info=(self.username, self.userpassword)
            print(info[1])
            con=connect()
            mycursor=connect()
            query = "SELECT firstname,lastname,username,password,accountID FROM account WHERE username = %s AND password = %s"
            mycursor[1].execute(query, info,)
            myresult = mycursor[1].fetchall()
            print(myresult)
            if self.userpassword and self.username in myresult[0]:
                self.namelabel.pack_forget()
                self.name.pack_forget()
                self.passwordlabel.pack_forget()
                self.password.pack_forget()
                self.button.pack_forget()
                log.destroy() #closes the window
                
                if '-M' in myresult[0][4]:
                    mywindow = ManagerAccount(myresult[0][0],myresult[0][1], myresult[0][3],myresult[0][2],myresult[0][4]).mainloop()
                else:
                    mywindow = Account().mainloop()
                
                
                return mywindow
            else: 
                return "incorrect Username or Password Entered"  

    def submit(self):
        self.userpassword=self.password.get()
        self.username=self.name.get()
        #print(f"The name entered by you is {self.username} {self.userpassword}")
        return self.login(self.username, self.userpassword) 

    def hide_label(self, event=None):
        self.label.lower(self.frame)
        self.entry.lower(self.frame)
   




log=LoginPage()
log.configure(bg='pink')
log.geometry("600x400")
log.mainloop()

