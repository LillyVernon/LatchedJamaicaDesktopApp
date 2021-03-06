from tkinter import *
from additems import AdditemsGUI
import tkinter as tk



class Order():
    def __init__(self):
        super().__init__()
         
            
        self.createorder()
    def additem(self):
            return AdditemsGUI().mainloop()

    def createorder(self):
        root = Tk()
        root.title('Order Summary')
        root.geometry("680x400")
        root.configure(bg='pink')
        master=root
        self.master=master
        self.myFrame = Frame(self.master)
        self.myFrame.grid()

        myLabel1 = Label(root,text="Latched Jamaica", bg="#f88379", width="50")
        myLabel1.grid(row=0, column=2)

        myLabel2 = Label(root, text="Order #1011   account ID")
        myLabel2.grid(row=1,column=2, pady=10)

        myLabel3 = Label(root, text="1 watch")
        myLabel3.grid(row=2,column=2)

        myLabel4 = Label(root, text="1 Earing")
        myLabel4.grid(row=3,column=2)

        myLabel5 = Label(root, text="1 Necklace")
        myLabel5.grid(row=4,column=2)

        myLabel5 = Label(root, text="Discount")
        myLabel5.grid(row=4,column=2)
        myLabel5 = Label(root, text="Total Price")
        myLabel5.grid(row=5,column=2)
     
        self.myButton1 = Button(master,text="Add Item",bg="#AEEEEE", width="20", command=self.additem)
        self.myButton1.grid(row=1,column=1,pady=20)

        self.myButton2 = Button(master,text="Apply Discount",bg="#AEEEEE",width="20")
        self.myButton2.grid(row=2,column=1, pady=20)

        self.myButton3 = Button(master,text="Delete Order",bg="#AEEEEE", width="20")
        self.myButton3.grid(row=3,column=1, pady=20)

        self.myButton4 = Button(master,text="Check out",bg="#AEEEEE", width="20")
        self.myButton4.grid(row=4,column=1, pady=20)

        self.myButton5 = Button(master,text="Sign out",bg="#f88379", width="20")
        self.myButton5.grid(row=6,column=5, pady=20)  
        
        

        
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


