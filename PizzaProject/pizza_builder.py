import abc
import sqlite3
from database import Database

db = Database()

with sqlite3.connect('pizza.db') as db:
    c = db.cursor()

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

class Pizza(metaclass = abc.ABCMeta):
	@abc.abstractmethod
	def get_price(self):
		pass

	@abc.abstractmethod
	def get_status(self):
		pass

class Base(Pizza):
	__base_price = 3

	def get_price(self):
		return self.__base_price

	def get_status(self):
		return "Dough"

class PizzaDecorator(Pizza):
	def __init__(self, pizza):
		self.pizza = pizza

	def get_price(self):
		return self.pizza.get_price()

	def get_status(self):
		return self.pizza.get_status()

class Italiano(Pizza):
	__pizza_price = get_pizza_price("Italiano")

	def get_price(self):
		return self.__pizza_price

	def get_status(self):
		return "Italiano"

class Pepperoni(Pizza):
	__pizza_price = get_pizza_price("Pepperoni")

	def get_price(self):
		return self.__pizza_price

	def get_status(self):
		return "Pepperoni"

class Supreme(Pizza):
	__pizza_price = get_pizza_price("Supreme")

	def get_price(self):
		return self.__pizza_price

	def get_status(self):
		return "Supreme"

class Tomato(PizzaDecorator):
	def __init__(self, pizza):
		super(Tomato, self).__init__(pizza)
		self.name = "Tomato"
		self.__tomato_price = get_extension_price(self.name)

	@property
	def price(self):
		return self.__tomato_price

	def get_price(self):
		return super(Tomato, self).get_price() + self.__tomato_price

	def get_status(self):
		return super(Tomato, self).get_status() + " + Tomato"

class Cheese(PizzaDecorator):
	def __init__(self, pizza):
		super(Cheese, self).__init__(pizza)
		self.__cheese_price = get_extension_price("Cheese")

	@property
	def price(self):
		return self.__cheese_price

	def get_price(self):
		return super(Cheese, self).get_price() + self.__cheese_price

	def get_status(self):
		return super(Cheese, self).get_status() + " + Cheese"

class Beef(PizzaDecorator):
	def __init__(self, pizza):
		super(Beef, self).__init__(pizza)
		self.__beef_price = get_extension_price("Beef")

	@property
	def price(self):
		return self.__beef_price

	def get_price(self):
		return super(Beef, self).get_price() + self.__beef_price

	def get_status(self):
		return super(Beef, self).get_status() + " + Beef"

class Mushroom(PizzaDecorator):
	def __init__(self, pizza):
		super(Mushroom, self).__init__(pizza)
		self.__mushroom_price = get_extension_price("Mushroom")

	@property
	def price(self):
		return self.__mushroom_price

	def get_price(self):
		return super(Mushroom, self).get_price() + self.__mushroom_price

	def get_status(self):
		return super(Mushroom, self).get_status() + " + Mushroom"

class Olive(PizzaDecorator):
	def __init__(self, pizza):
		super(Olive, self).__init__(pizza)
		self.__olive_price = get_extension_price("Olive")

	@property
	def price(self):
		return self.__olive_price

	def get_price(self):
		return super(Olive, self).get_price() + self.__olive_price

	def get_status(self):
		return super(Olive, self).get_status() + " + Olive"

class PizzaBuilder:
	def __init__(self, pizza_type):
		self.pizza_type = pizza_type
		self.pizza = eval(pizza_type)()
		self.extensions_list = []

	def add_extension(self, extension):
		self.pizza = eval(extension)(self.pizza)
		self.extensions_list.append(extension)

	def remove_extension(self, extension):
		if extension in self.extensions_list:
			self.extensions_list.remove(extension)

		temp_pizza = eval(self.pizza_type)()
		for ex in self.extensions_list:
			temp_pizza = eval(ex)(temp_pizza)

		self.pizza = temp_pizza

	def get_price(self):
		return self.pizza.get_price()

	def get_status(self):
		return self.pizza.get_status()
