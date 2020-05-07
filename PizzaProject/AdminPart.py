from tkinter import *
import sqlite3
from pizza_builder import PizzaBuilder
from tkinter import messagebox as ms
from tkinter import ttk

with sqlite3.connect('pizza.db') as db:
	c = db.cursor()


class Admin:
	def __init__(self):
		self.username = "admin"
		self.password = "admin"
		self.admin_page = Toplevel()
		self.admin_page.title("ADMIN PAGE")
		self.admin_page.geometry("800x500")
		self.AdminFrame = Frame(master = self.admin_page, bg = "gold", bd = 5)
		self.AdminFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
		Label(master = self.AdminFrame, 
			text = "WELCOME TO ADMIN PAGE", fg = "red", 
			bg = "gold", font = ('', 20, 'bold')).pack()
		Button(master = self.AdminFrame, 
			text = "Create New Pizza", bg = "orange", height = 2, width = 12, 
			relief = RAISED, command = lambda:NewPizza()).place(x = 125, y = 110)
		Button(master = self.AdminFrame, 
			text = "See All Orders", bg = "orange", height = 2, width = 12, 
			relief = RAISED, command = lambda:AllOrders()).place(x = 550, y = 110)
		self.admin_page.mainloop()

	def get_extension_price(extension_name: str) -> str:
		statement = "SELECT * FROM extensions WHERE ExtensionTitle = ?"
		c.execute(statement, (extension_name, ))
		price = int(c.fetchone()[2])
		return price

	def get_pizza_price(pizza_name: str) -> str:
		statement = "SELECT * FROM pizzas WHERE PizzaName = ?"
		c.execute(statement, (pizza_name, ))
		price = int(c.fetchone()[3])
		return price

	def add_to_database(pizzaID, pizzaName, pizzaRecipe, pizzaPrice):
		find_pizzaID = "SELECT * FROM pizzas WHERE PizzaID = ?"
		find_pizzaName = "SELECT * FROM pizzas WHERE PizzaName = ?"
		find_pizzaRecipe = "SELECT * FROM pizzas WHERE PizzaRecipe = ?"
		c.execute(find_pizzaID, (pizzaID, ))
		result_id = c.fetchall()
		c.execute(find_pizzaName, (pizzaName, ))
		result_name = c.fetchall()
		c.execute(find_pizzaRecipe, (pizzaRecipe, ))
		result_recipe = c.fetchall()
		if result_id or result_name or result_recipe:
			ms.showerror("ERROR!", "THIS PIZZA EXISTS!")
		else:
			ms.showinfo("SUCCESS!", "PIZZA ADDED TO DATABASE!")
			statement = "INSERT INTO pizzas(PizzaID, PizzaName, PizzaRecipe, PizzaPrice) VALUES (?, ?, ?, ?)"
			c.execute(statement, [(pizzaID), (pizzaName), (pizzaRecipe), (pizzaPrice)])
			db.commit()
			

class NewPizza:
	def __init__(self):
		self.pizza_id = StringVar()
		self.pizza_name = StringVar()
		self.NewPizzaPage = Toplevel()
		self.NewPizzaPage.title("New Pizza Creation")
		self.NewPizzaPage.geometry("860x650")
		self.NewPizzaFrame = Frame(master = self.NewPizzaPage, bg = "gold",  bd = 5)
		self.NewPizzaFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)

		Label(master = self.NewPizzaFrame, text = "PIZZA CREATOR", bg = "gold", fg = "red", font = ('', 20, 'bold')).pack()

		self.pizza = PizzaBuilder("Base")

		Button(master = self.NewPizzaFrame, bg = "red", 
			command = lambda:[self.pizza.add_extension("Tomato"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Add Tomato", width = 14).place(x = 40, y = 60)
		Button(master = self.NewPizzaFrame, bg = "red", 
			command = lambda:[self.pizza.remove_extension("Tomato"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Remove Tomato", width = 14).place(x = 40, y = 120)
		Button(master = self.NewPizzaFrame, bg = "yellow", 
			command = lambda:[self.pizza.add_extension("Cheese"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Add Cheese", width = 14).place(x = 200, y = 60)
		Button(master = self.NewPizzaFrame, bg = "yellow", 
			command = lambda:[self.pizza.remove_extension("Cheese"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Remove Cheese", width = 14).place(x = 200, y = 120)
		Button(master = self.NewPizzaFrame, bg = "firebrick", fg = "wheat", 
			command = lambda:[self.pizza.add_extension("Beef"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Add Beef", width = 14).place(x = 360, y = 60)
		Button(master = self.NewPizzaFrame, bg = "firebrick", fg = "wheat", 
			command = lambda:[self.pizza.remove_extension("Beef"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Remove Beef", width = 14).place(x = 360,  y = 120)
		Button(master = self.NewPizzaFrame, bg = "wheat", 
			command = lambda:[self.pizza.add_extension("Mushroom"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Add Mushroom", width = 14).place(x = 520, y = 60)
		Button(master = self.NewPizzaFrame, bg = "wheat", 
			command = lambda:[self.pizza.remove_extension("Mushroom"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Remove Mushroom", width = 14).place(x = 520, y = 120)
		Button(master = self.NewPizzaFrame, bg = "black", fg = "wheat", 
			command = lambda:[self.pizza.add_extension("Olive"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Add Olive", width = 14).place(x = 680, y =  60)
		Button(master = self.NewPizzaFrame, bg = "black", fg = "wheat", 
			command = lambda:[self.pizza.remove_extension("Olive"), self.display_recipe(self.NewPizzaFrame), self.display_price(self.NewPizzaFrame)], 
			text = "Remove Olive", width = 14).place(x = 680, y = 120)
		
		
		Label(master = self.NewPizzaFrame, 
			text = "Enter Pizza ID", 
			bg = "gold", fg = "red").place(x = 95, y = 180)
		Entry(master = self.NewPizzaFrame, 
			textvariable = self.pizza_id).place(x = 60, y = 200)
		Label(master = self.NewPizzaFrame, 
			text = "Enter Pizza Name", 
			bg = "gold", fg = "red").place(x = 85, y = 240)
		Entry(master = self.NewPizzaFrame, 
			textvariable = self.pizza_name).place(x = 60, y = 260)
		Label(master = self.NewPizzaFrame, 
			text = "Pizza Recipe", 
			bg = "gold", fg = "red").place(x = 395, y = 180)
		Label(master = self.NewPizzaFrame, 
			text = "Pizza Price", 
			bg = "gold", fg = "red").place(x = 695, y = 180)


		Button(master = self.NewPizzaFrame, 
			bg = "orange", width = 15, height = 2, 
			text = "Add to Database", 
			command = lambda:Admin.add_to_database(self.pizza_id.get(), self.pizza_name.get(), self.pizza.get_status(), self.pizza.get_price())).place(x = 360, y = 360)
		
		self.NewPizzaPage.mainloop()

	def display_recipe(self, root):
		textbox = Text(master = root, width = 30, height = 7.5)
		textbox.place(x = 320, y = 200)
		textbox.insert(END, f"{self.pizza.get_status()}")

	def display_price(self, root):
		textbox = Text(master = root, width = 20, height = 1)
		textbox.place(x = 645, y = 200)
		textbox.insert(END, f"{self.pizza.get_price()} AZN")


class AllOrders:
	def __init__(self):

		self.OrdersPage = Toplevel()
		self.OrdersPage.title("ORDERS")
		self.OrdersPage.geometry("1200x1000")

		c.execute("SELECT * FROM orders")
		rows = c.fetchall()

		self.tree = ttk.Treeview(master = self.OrdersPage, height = 10, columns = ('#0', '#1', '#2', '#3', '#4'))
		self.tree.grid(row = 5, column = 5, columnspan = 5)
		self.tree.heading('#0', text = "OrderID", anchor = W)
		self.tree.heading('#1', text = "OrderDate", anchor = W)
		self.tree.heading('#2', text = "Username", anchor = W)
		self.tree.heading('#3', text = "OrderContent", anchor = W)
		self.tree.heading('#4', text = "Payment", anchor = W)

		records = self.tree.get_children()
		totalsum = 0

		for record in records:
			self.tree.delete(record)
		for row in rows:
			totalsum += row[4]
			self.tree.insert('', 0, text = row[0], values = (row[1], row[2], row[3], row[4]))
		self.tree.heading('#5', text = f"Total Sum:  {totalsum}", anchor = W)

		self.tree.place(x = 0, y = 0, relheight = 1, relwidth = 1)

		self.scrollbar = Scrollbar(master = self.OrdersPage)
		self.scrollbar.pack(side = RIGHT, fill = Y)
		self.scrollbar.config(command = self.tree.yview)

		self.OrdersPage.mainloop()

