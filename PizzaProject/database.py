import sqlite3

with sqlite3.connect('pizza.db') as db:
	c = db.cursor()

class Database:
	def __init__(self):

		c.execute("""CREATE TABLE IF NOT EXISTS users (
					username text, 
					password text,
					name text,
					surname text
					)""")
		db.commit()

		c.execute("""CREATE TABLE IF NOT EXISTS orders (
					OrderID INTEGER PRIMARY KEY, 
					OrderDate TEXT NOT NULL,
					Username TEXT NOT NULL,
					OrderContent TEXT NOT NULL,
					Payment INTEGER NOT NULL
					)""")
		db.commit()

		c.execute("""CREATE TABLE IF NOT EXISTS pizzas (
					PizzaID INTEGER,
					PizzaName TEXT NOT NULL,
					PizzaRecipe TEXT NOT NULL,
					PizzaPrice INTEGER
					)""")

		db.commit()

		c.execute("""CREATE TABLE IF NOT EXISTS extensions (
					ExtensionID INTEGER,
					ExtensionTitle TEXT NOT NULL,
					ExtensionPrice INTEGER
					)""")

		db.commit()

		c.execute("SELECT * FROM users")
		if not c.fetchall():
			c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", ("admin", "admin", "Admin", "Admin"))
			db.commit()

		c.execute("SELECT * FROM pizzas")
		if not c.fetchall():
			self.add_pizza(131, "Italiano", "Italiano Pizza", 15)
			self.add_pizza(121, "Pepperoni", "Pepperoni Pizza", 18)
			self.add_pizza(101, "Supreme", "Supreme Pizza", 20)

		c.execute("SELECT * FROM extensions")
		if not c.fetchall():
			self.add_extension(111, "Tomato", 1)
			self.add_extension(222, "Cheese", 1)
			self.add_extension(333, "Beef", 3)
			self.add_extension(444, "Mushroom", 2)
			self.add_extension(555, "Olive", 2)

	def add_pizza(self, pizzaid, pizzaname, pizzarecipe, pizzaprice):
		c.execute("INSERT INTO pizzas VALUES (?, ?, ?, ?)", (pizzaid, pizzaname, pizzarecipe, pizzaprice))
		db.commit()

	def add_extension(self, extensionid, extensiontitle, extensionprice):
		c.execute("INSERT INTO extensions VALUES (?, ?, ?)", (extensionid, extensiontitle, extensionprice))
		db.commit()

