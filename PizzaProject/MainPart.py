from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import ImageTk, Image
from AdminPart import Admin, NewPizza
from tkinter import ttk
from pizza_builder import PizzaBuilder
import datetime
from HashPasswordVerifier import Hash

with sqlite3.connect('pizza.db') as db:
    c = db.cursor()

USER = ""

class Root:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("800x500")
        self.root.title("TAPDIG'S PIZZA SHOP")
        self.frame = Frame(master = self.root, bg = "gold", bd = 5, width = 20, height = 20)
        self.frame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.label = Label(master = self.frame, text = "WELCOME TO PIZZA SHOP", bg = "gold", fg = "red", font = ('', 20, 'bold'))
        self.label.pack(fill = BOTH)
        self.NewOrderButton = Button(master = self.frame, text = "New Order", bg = "orange", relief = RAISED, height = 2, width = 12, command = lambda:NewOrder())
        self.NewOrderButton.place(x = 125, y = 110)
        self.PastOrdersButton = Button(master = self.frame, text = "See Past Orders", bg = "orange", relief = RAISED, height = 2, width = 12, command = lambda:PastOrders())
        self.PastOrdersButton.place(x = 550, y = 110)
        self.canvas = Canvas(self.frame, bg = "gold", width = 200, height = 200)
        self.canvas.pack()
        self.logo = PhotoImage(file = r"Photos/logo.png")
        self.canvas.create_image(100, 100, image = self.logo)
        self.root.mainloop()

class NewOrder:
    def __init__(self):
        self.order_list = {}
        self.content = ""
        self.price = 0
        
        self.window = Toplevel()
        self.window.geometry("1070x1000")
        self.window.title("NEW ORDER")
        self.NewOrderFrame = Frame(master = self.window, bg = "gold", bd = 5)
        self.NewOrderFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.canvas1 = Canvas(self.NewOrderFrame, bg = "gold", width = 350, height = 320)
        self.canvas1.grid(row = 0, column = 0)
        self.italiano = PhotoImage(file = r"Photos/italiano.png")
        self.pizza_italiano = PizzaBuilder("Italiano")
        Label(master = self.NewOrderFrame, 
            bg = "red",  fg = "yellow", padx = 5, pady = 5, 
            text = "ITALIANO", font = ("", 20)).grid(row = 0, column = 0, sticky = N)
        Label(master = self.NewOrderFrame, 
            bg = "red", fg = "yellow", padx = 5, pady = 5, 
            text = f"{Admin.get_pizza_price('Italiano')} AZN", font = ("", 15)).grid(row = 0, column = 0, sticky = S)
        self.canvas1.create_image(170, 170, image = self.italiano)

        self.canvas2 = Canvas(self.NewOrderFrame, bg = "gold", width = 350, height = 320)
        self.canvas2.grid(row = 0, column = 6)
        self.pepperoni = PhotoImage(file = r"Photos/pepperoni.png")
        self.pizza_pepperoni = PizzaBuilder("Pepperoni")
        Label(master = self.NewOrderFrame, 
            bg = "red",  fg = "yellow", padx = 5, pady = 5, 
            text = "PEPPERONI", font = ("", 20)).grid(row = 0, column = 6, sticky = N)
        Label(master = self.NewOrderFrame, 
            bg = "red",  fg = "yellow", padx = 5, pady = 5, 
            text = f"{Admin.get_pizza_price('Pepperoni')} AZN", font = ("", 15)).grid(row = 0, column = 6, sticky = S)
        self.canvas2.create_image(170, 170, image = self.pepperoni)

        self.canvas3 = Canvas(self.NewOrderFrame, bg = "gold", width = 350, height = 320)
        self.canvas3.grid(row = 0, column = 8)
        self.supreme = PhotoImage(file = r"Photos/supreme.png")
        self.pizza_supreme = PizzaBuilder("Supreme")
        Label(master = self.NewOrderFrame, 
            bg = "red", fg = "yellow",  padx = 5, pady = 5, 
            text = "SUPREME", font = ("", 20)).grid(row = 0, column = 8, sticky = N)
        Label(master = self.NewOrderFrame, 
            bg = "red",  fg = "yellow", padx = 5, pady = 5, 
            text = f"{Admin.get_pizza_price('Supreme')} AZN", font = ("", 15)).grid(row = 0, column = 8, sticky = S)
        self.canvas3.create_image(170, 170, image = self.supreme)

        Text(master = self.NewOrderFrame, width = 50, height = 4).place(x = 325, y = 750)
        Text(master = self.NewOrderFrame, width = 10, height = 2).place(x = 500, y = 830)

        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Tomato')} AZN", 
            bg = "red", fg = "yellow").place(x = 60, y = 335)
        Button(master =  self.NewOrderFrame, 
            text = "Add Tomato", width = 10, bg = "red",
            command = lambda:self.pizza_italiano.add_extension("Tomato")).place(x = 120, y =330)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Cheese')} AZN",
            bg = "red", fg = "yellow").place(x = 60, y = 375)
        Button(master =  self.NewOrderFrame, 
            text = "Add Cheese", width = 10, bg = "yellow", 
            command = lambda:self.pizza_italiano.add_extension("Cheese")).place(x = 120, y =370)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Beef')} AZN", 
            bg = "red", fg = "yellow").place(x = 60, y = 415)
        Button(master =  self.NewOrderFrame, 
            text = "Add Beef", width = 10, bg = "firebrick", fg = "wheat", 
            command = lambda:self.pizza_italiano.add_extension("Beef")).place(x = 120, y =410)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Mushroom')} AZN", 
            bg = "red", fg = "yellow").place(x = 60, y = 455)
        Button(master =  self.NewOrderFrame, 
            text = "Add Mushroom", width = 10, bg = "wheat", 
            command = lambda:self.pizza_italiano.add_extension("Mushroom")).place(x = 120, y =450)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Olive')} AZN", 
            bg = "red", fg = "yellow").place(x = 60, y = 495)
        Button(master =  self.NewOrderFrame, 
            text = "Add Olive", width = 10, bg = "black", fg = "wheat", 
            command = lambda:self.pizza_italiano.add_extension("Olive")).place(x = 120, y =490)
        
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Tomato')} AZN", 
            bg = "red", fg = "yellow").place(x = 415, y = 335)
        Button(master =  self.NewOrderFrame, 
            text = "Add Tomato", width = 10, bg = "red", 
            command = lambda:self.pizza_pepperoni.add_extension("Tomato")).place(x = 475, y =330)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Cheese')} AZN", 
            bg = "red", fg = "yellow").place(x = 415, y = 375)
        Button(master =  self.NewOrderFrame, 
            text = "Add Cheese", width = 10, bg = "yellow", 
            command = lambda:self.pizza_pepperoni.add_extension("Cheese")).place(x = 475, y =370)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Beef')} AZN", 
            bg = "red", fg = "yellow").place(x = 415, y = 415)
        Button(master =  self.NewOrderFrame, 
            text = "Add Beef", width = 10, bg = "firebrick", fg = "wheat", 
            command = lambda:self.pizza_pepperoni.add_extension("Beef")).place(x = 475, y =410)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Mushroom')} AZN", 
            bg = "red", fg = "yellow").place(x = 415, y = 455)
        Button(master =  self.NewOrderFrame, 
            text = "Add Mushroom", width = 10, bg = "wheat", 
            command = lambda:self.pizza_pepperoni.add_extension("Mushroom")).place(x = 475, y =450)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Olive')} AZN", 
            bg = "red", fg = "yellow").place(x = 415, y = 495)
        Button(master =  self.NewOrderFrame, 
            text = "Add Olive", width = 10, bg = "black", fg = "wheat", 
            command = lambda:self.pizza_pepperoni.add_extension("Olive")).place(x = 475, y =490)
        
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Tomato')} AZN", 
            bg = "red", fg = "yellow").place(x = 765, y = 335)
        Button(master =  self.NewOrderFrame, 
            text = "Add Tomato", width = 10, bg = "red", 
            command = lambda:self.pizza_supreme.add_extension("Tomato")).place(x = 825, y =330)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Cheese')} AZN", 
            bg = "red", fg = "yellow").place(x = 765, y = 375)
        Button(master =  self.NewOrderFrame, 
            text = "Add Cheese", width = 10, bg = "yellow", 
            command = lambda:self.pizza_supreme.add_extension("Cheese")).place(x = 825, y =370)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Beef')} AZN", 
            bg = "red", fg = "yellow").place(x = 765, y = 415)
        Button(master =  self.NewOrderFrame, 
            text = "Add Beef", width = 10, bg = "firebrick", fg = "wheat", 
            command = lambda:self.pizza_supreme.add_extension("Beef")).place(x = 825, y =410)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Mushroom')} AZN", 
            bg = "red", fg = "yellow").place(x = 765, y = 455)
        Button(master =  self.NewOrderFrame, 
            text = "Add Mushroom", width = 10, bg = "wheat", 
            command = lambda:self.pizza_supreme.add_extension("Mushroom")).place(x = 825, y =450)
        Label(master = self.NewOrderFrame, 
            text = f"{Admin.get_extension_price('Olive')} AZN", 
            bg = "red", fg = "yellow").place(x = 765, y = 495)
        Button(master =  self.NewOrderFrame, 
            text = "Add Olive", width = 10, bg = "black", fg = "wheat", 
            command = lambda:self.pizza_supreme.add_extension("Olive")).place(x = 825, y =490)

        Button(master = self.NewOrderFrame, 
            text = "Build Your Own Pizza",  
            bg = "orange", height = 5, width = 35, fg = "red", font = ('', 10, 'bold'), 
            command = lambda:self.BuildPizza()).place(x = 80, y = 630)
        Button(master = self.NewOrderFrame, 
            text = "See New Pizzas by Admin",  
            bg = "orange", height = 5, width = 35, fg = "red", font = ('', 10, 'bold'), 
            command = lambda:self.SeeNewPizzas()).place(x = 630, y = 630)

        Button(master = self.NewOrderFrame, 
            bg = "orange", text = "Add to Basket", height = 2, 
            command = lambda:[self.add_to_basket(self.pizza_italiano.get_status(), self.pizza_italiano.get_price()), self.show_order_info()]).place(x = 115, y = 540)
        Button(master = self.NewOrderFrame, 
            bg = "orange", text = "Add to Basket", height = 2, 
            command = lambda:[self.add_to_basket(self.pizza_pepperoni.get_status(), self.pizza_pepperoni.get_price()), self.show_order_info()]).place(x = 470, y = 540)
        Button(master = self.NewOrderFrame, 
            bg = "orange", text = "Add to Basket", height = 2, 
            command = lambda:[self.add_to_basket(self.pizza_supreme.get_status(), self.pizza_supreme.get_price()), self.show_order_info()]).place(x = 820, y = 540)

        global USER
        Button(master = self.NewOrderFrame, 
            bg = "orange", text = "Confirm Order", font = ('', 10, 'bold'), height = 3, width = 15, 
            command = lambda:self.confirm_order(USER)).place(x = 320, y = 880)
        Button(master = self.NewOrderFrame, 
            bg = "orange", text = "Cancel Order", font = ('', 10, 'bold'), height = 3, width = 15, 
            command = lambda:self.cancel_order()).place(x = 600, y = 880)

        Label(master = self.NewOrderFrame, 
            bg = "gold", text = "BASKET: ", fg = "red", font = ('', 12, 'bold')).place(x = 240, y = 775)
        Label(master = self.NewOrderFrame, 
            bg = "gold", text = "Total Sum: ", fg = "red", font = ('', 12, 'bold')).place(x = 390, y = 840)

        self.window.mainloop()

    def show_order_info(self):
        textbox_content = Text(master = self.NewOrderFrame, width = 50, height = 4)
        textbox_content.place(x = 325, y = 750)
        textbox_content.insert(END, f"{self.content}")
        textbox_price = Text(master = self.NewOrderFrame, width = 10, height = 2)
        textbox_price.place(x = 500, y = 830)
        textbox_price.insert(END, f"{self.price}")

    def add_to_basket(self, content, payment):
        self.order_list[payment] = content
        self.content += (" | " + content)
        self.price += payment

    def confirm_order(self, UserName):

        with sqlite3.connect('pizza.db') as db:
            c = db.cursor()

        statement = "INSERT INTO orders (OrderDate, Username, OrderContent, Payment) VALUES (?, ?, ?, ?)"
        if self.content != "" and self.price != 0:
            c.execute(statement, [(datetime.datetime.now()), (UserName), (self.content), (self.price)])
            db.commit()
            ms.showinfo("ORDER INFO", "SUCCESSFULLY ORDERED!")
            self.window.destroy()
        else:
            ms.showerror("NOTHING ORDERED", "Basket is empty, choose something to order!")

    def cancel_order(self):
        self.order_list = {}
        self.content = ""
        self.price = 0
        ms.showinfo("CANCELLATION", "ORDER CANCELLED!")
        Text(master = self.NewOrderFrame, width = 50, height = 4).place(x = 325, y = 750)
        Text(master = self.NewOrderFrame, width = 10, height = 2).place(x = 500, y = 830)

    def BuildPizza(self):

        self.BuildWindow = Toplevel()
        self.BuildWindow.title("Build Your Own Pizza")
        self.BuildWindow.geometry("860x650")
        self.BuildPizzaFrame = Frame(master = self.BuildWindow, bg = "gold",  bd = 5)
        self.BuildPizzaFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        Label(master = self.BuildPizzaFrame, 
            text = "BUILD YOUR PIZZA", 
            bg = "gold", fg = "red", font = ('', 20, 'bold')).pack()

        self.pizza = PizzaBuilder("Base")

        Button(master = self.BuildPizzaFrame, 
            bg = "red", 
            command = lambda:[self.pizza.add_extension("Tomato"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Add Tomato", width = 14).place(x = 40, y = 60)
        Button(master = self.BuildPizzaFrame, 
            bg = "red", 
            command = lambda:[self.pizza.remove_extension("Tomato"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Remove Tomato", width = 14).place(x = 40, y = 120)
        Button(master = self.BuildPizzaFrame, 
            bg = "yellow", 
            command = lambda:[self.pizza.add_extension("Cheese"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Add Cheese", width = 14).place(x = 200, y = 60)
        Button(master = self.BuildPizzaFrame, 
            bg = "yellow", 
            command = lambda:[self.pizza.remove_extension("Cheese"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Remove Cheese", width = 14).place(x = 200, y = 120)
        Button(master = self.BuildPizzaFrame, 
            bg = "firebrick", fg = "wheat", 
            command = lambda:[self.pizza.add_extension("Beef"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Add Beef", width = 14).place(x = 360, y = 60)
        Button(master = self.BuildPizzaFrame, 
            bg = "firebrick", fg = "wheat", 
            command = lambda:[self.pizza.remove_extension("Beef"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Remove Beef", width = 14).place(x = 360,  y = 120)
        Button(master = self.BuildPizzaFrame, 
            bg = "wheat", 
            command = lambda:[self.pizza.add_extension("Mushroom"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Add Mushroom", width = 14).place(x = 520, y = 60)
        Button(master = self.BuildPizzaFrame, 
            bg = "wheat", 
            command = lambda:[self.pizza.remove_extension("Mushroom"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Remove Mushroom", width = 14).place(x = 520, y = 120)
        Button(master = self.BuildPizzaFrame, 
            bg = "black", fg = "wheat", 
            command = lambda:[self.pizza.add_extension("Olive"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Add Olive", width = 14).place(x = 680, y =  60)
        Button(master = self.BuildPizzaFrame, 
            bg = "black", fg = "wheat", 
            command = lambda:[self.pizza.remove_extension("Olive"), NewPizza.display_recipe(self, self.BuildPizzaFrame), NewPizza.display_price(self, self.BuildPizzaFrame)], 
            text = "Remove Olive", width = 14).place(x = 680, y = 120)

        Label(master = self.BuildPizzaFrame, 
            text = "Pizza Recipe", 
            bg = "gold", fg = "red").place(x = 395, y = 180)
        Label(master = self.BuildPizzaFrame, 
            text = "Pizza Price", 
            bg = "gold", fg = "red").place(x = 695, y = 180)

        Button(master = self.BuildPizzaFrame, 
            bg = "orange", width = 15, height = 2, text = "Add to Basket", 
            command = lambda:[self.add_to_basket(self.pizza.get_status(), self.pizza.get_price()), self.show_order_info()]).place(x = 280, y = 360)
        Button(master = self.BuildPizzaFrame, 
            bg = "orange", width = 15, height = 2, text = "Back to Order Page", 
            command = lambda:self.BuildWindow.destroy()).place(x = 440, y = 360)
        self.BuildWindow.mainloop()

    def SeeNewPizzas(self):
        self.AdminsPizzas = Toplevel()
        self.AdminsPizzas.title("NEW RECIPES BY ADMIN")
        self.AdminsPizzas.geometry("1000x1000")
        self.AdminsPizzasFrame = Frame(master = self.AdminsPizzas, bg = "gold", bd = 5)
        self.AdminsPizzasFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        Label(master = self.AdminsPizzasFrame, 
            bg = "gold", fg = "red", font = ('', 20, 'bold'), 
            text = "NEW RECIPES BY ADMIN").pack()


        Label(master = self.AdminsPizzasFrame, 
            bg = "gold", fg = "black", font = ('', 15, 'bold'), 
            text = "Pizza Name").place(x = 10, y = 75)
        Label(master = self.AdminsPizzasFrame, 
            bg = "gold", fg = "black", font = ('', 15, 'bold'), 
            text = "Pizza Recipe").place(x = 330, y = 75)
        Label(master = self.AdminsPizzasFrame, 
            bg = "gold", fg = "black", font = ('', 15, 'bold'), 
            text = "Pizza Price").place(x = 650, y = 75)

        c.execute("SELECT * FROM pizzas")
        rows = c.fetchall()

        for i in range(3, len(rows)):
            row = rows[i]
            recipe = row[2]
            price = row[3]
            Label(master = self.AdminsPizzasFrame, 
                bg = "red", fg = "yellow", 
                text = f"{row[1]}").place(x = 10, y = i * 45)
            textbox = Text(master = self.AdminsPizzasFrame, width = 60, height = 2)
            textbox.place(x = 170, y = i * 45)
            textbox.insert(END, f"{row[2]}")
            Label(master = self.AdminsPizzasFrame, 
                bg = "red", fg = "yellow", 
                text = f"{row[3]}").place(x = 700, y = i * 45)
            Button(master = self.AdminsPizzasFrame, 
                bg = "orange", text = "Add to Basket", 
                command = lambda recipe =  recipe, price = price:[self.add_to_basket(recipe, price), self.show_order_info(), self.show_info()]).place(x = 770, y = i * 45)

    def show_info(self):
        ms.showinfo("Success", "Order added to basket!")
        self.AdminsPizzas.destroy()

class PastOrders:
    def __init__(self):
        global USER
        self.username = USER
        self.page = Toplevel()
        self.page.title("PAST ORDERS")
        self.page.geometry("1000x1000")
        self.PastOdersFrame = Frame(master = self.page, bg = "gold", bd = 5)
        self.PastOdersFrame.place(x = 0, y = 0, relheight = 1, relwidth = 1)
    
        c.execute("SELECT * FROM orders WHERE username = ?", (self.username, ))
        rows = c.fetchall()

        self.tree = ttk.Treeview(master = self.PastOdersFrame, height = 10, columns = ('#0', '#1', '#2', '#3', '#4'))
        self.tree.grid(row = 5, column = 5, columnspan = 5)
        self.tree.heading('#0', text = "OrderID", anchor = W)
        self.tree.heading('#1', text = "OrderDate", anchor = W)
        self.tree.heading('#2', text = "Username", anchor = W)
        self.tree.heading('#3', text = "OrderContent", anchor = W)
        self.tree.heading('#4', text = "Payment", anchor = W)
        records = self.tree.get_children()
        for record in records:
            self.tree.delete(record)
        for row in rows:
            self.tree.insert('', 0, text = row[0], values = (row[1], row[2], row[3], row[4]))
        self.tree.place(x = 0, y = 0, relheight = 1, relwidth = 1)

        self.scrollbar = Scrollbar(master = self.page)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.scrollbar.config(command = self.tree.yview)

        self.page.mainloop()

class Main:
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.name = StringVar()
        self.surname = StringVar()
        self.new_username = StringVar()
        self.new_password = StringVar()
        self.widgets()

    def login(self):
        global USER
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.app = Admin()
        else:
            c.execute("SELECT * FROM users WHERE username = ?", (self.username.get(), ))
            self.stored_password = c.fetchone()[1]
            find_user = ('SELECT * FROM users WHERE username = ? and password = ?')
            c.execute(find_user,[(self.username.get()),(Hash.verify_password(self.stored_password, self.password.get()))])
            USER = self.username.get()
            result = c.fetchall()
            if self.username.get() != "admin" and result:
                self.login_frame.pack_forget()
                self.app = Root()
            else:
                ms.showerror('Oops!','Username or Password is wrong.')
            
    def new_user(self):
        find_user = ('SELECT * FROM users WHERE username = ?')
        c.execute(find_user,[(self.new_username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            insert = 'INSERT INTO users(username,password, name, surname) VALUES(?,?, ?, ?)'
            c.execute(insert,[(self.new_username.get()),(Hash.hash_password(self.new_password.get())), (self.name.get()), (self.surname.get())])
            db.commit()
            self.log()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.register_frame.pack_forget()
        self.head['text'] = 'LOGIN'
        self.login_frame.pack()

    def create(self):
        self.new_username.set('')
        self.new_password.set('')
        self.name.set('')
        self.surname.set('')
        self.login_frame.pack_forget()
        self.head['text'] = "REGISTRATION"
        self.register_frame.pack()
  
    def widgets(self):
        self.head = Label(self.master,text = "WELCOME TO TAPDIG'S PIZZA SHOP", bg = "gold", fg = "red", font = ('',15, "bold"),pady=15)
        self.head.pack()
        self.login_frame = Frame(self.master,padx =30,pady = 30, bg = "lime")
        Label(self.login_frame,text = 'Username: ',fg = "red", bg = "lime", font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.login_frame,textvariable = self.username,bd = 5, font = ('',10)).grid(row=1,column=0, sticky = NSEW)
        Label(self.login_frame,text = 'Password: ', bg = "lime", fg = "red", font = ('',15),pady=5,padx=5).grid(sticky = W)
        Entry(self.login_frame,textvariable = self.password,bd = 5, font = ('',10),show = '*').grid(row=3,column=0, sticky = NSEW)
        Button(self.login_frame,text = ' Login ',bd = 3 , bg = "orange", font = ('',10),padx=5,pady=10,command=self.login).grid(row = 4, column = 0)
        Button(self.login_frame,text = ' Create Account ',bd = 3, bg = "orange", font = ('',10),padx=5,pady=5,command=self.create).grid(row=4,column=1)
        self.login_frame.pack()
        
        self.register_frame = Frame(self.master,padx =25,pady = 0, bg = "lime")
        Label(self.register_frame,text = 'Username: ', fg = "red", bg = "lime", font = ('',10),pady=5,padx=5).grid(sticky = NSEW)
        Entry(self.register_frame,textvariable = self.new_username,bd = 5,font = ('',10)).grid(row=1,column=0)
        Label(self.register_frame,text = 'Password: ',fg = "red", bg = "lime", font = ('',10),pady=5,padx=5).grid(sticky = NSEW)
        Entry(self.register_frame,textvariable = self.new_password,bd = 5,font = ('',10),show = '*').grid(row=3,column=0)
        Label(self.register_frame,text = 'Name: ', fg = "red", bg = "lime", font = ('',10),pady=5,padx=5).grid(sticky = NSEW)
        Entry(self.register_frame,textvariable = self.name,bd = 5,font = ('',10)).grid(row=5,column=0)
        Label(self.register_frame,text = 'Surname: ', fg = "red", bg = "lime", font = ('',10),pady=5,padx=5).grid(sticky = NSEW)
        Entry(self.register_frame,textvariable = self.surname,bd = 5,font = ('',10)).grid(row=7,column=0)
        Button(self.register_frame,text = 'Create Account',bg = "orange", bd = 3 ,font = ('',10),padx=5,pady=5,command=self.new_user).grid(row = 10, column = 0)
        Button(self.register_frame,text = 'Go to Login', bg = "orange", bd = 3 ,font = ('',10),padx=5,pady=5,command=self.log).grid(row = 10, column = 1)

