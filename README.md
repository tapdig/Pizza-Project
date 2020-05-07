# 🍕  PIZZA PROJECT 🍕
This is a simple **pizza ordering project** made by using technologies such as Python3, SQLite3 for database, and Tkinter for GUI. Pizzas are built with the help of Decorator design pattern.
    
# CONTENTS
1.  [ Prerequisites ](#desc)  
2. [ Installation](#usage)  
3. [Built with](#built)
4. [Author](#author)
  
<a  name="desc"></a>  
## Prerequisites
    sudo apt-get install python3-tk
    pip install pysqlite3 
	python3 -m pip install Pillow

<a  name="usage"></a>  
## Installation
Make sure to download all the files. "pizza.db" has been added, but it would be automatically established once the "main.py" code is executed.

    python3 main.py
    
<a  name="built"></a>  
## Built with

 - Python
 - SQLite
 - Tkinter
<a  name="author"></a>  
## Author
**Tapdig Maharramli**

# DESCRIPTION
1.  [ Login or Registration Page ](#log)  
2. [ User's Page](#user)  
3. [Admin's Page](#admin)

<a  name="log"></a> 
## Login or Registration Page
User is prompted to enter his/her username and password. If he/she does not have an account, then click "Create Account" button and fill the required credentials. Note that, passwords are not kept as plain text in the database. Once registered, hashed password will be stored in the database. 
> **Admin:** In order to switch to admin page -> username: **admin** | password: **admin**

<a  name="user"></a>
## User's Page
 "See Past Orders" button is for the user to view his/her past orders with details. **"New Order"** button is for the user to order new pizzas. User can choose from default pizzas, add extensions to them and must click **"Add to Basket"** button. **"Build Your Own Pizza"** is for the user to create the pizza as he/she desires by adding extensions. User must click "Add to Basket" and "Back to Order Page". Also user can view new recipes added by admin by clicking **"See New Pizzas by Admin"** button. The content and price of the order is shown during the **real-time**. User can confirm or cancel the chosen pizzas.

<a  name="admin"></a>
## Admin's Page
Admin is able to view all the past orders and see **total sum he/she earned** by clicking to the **"See All Orders"**. Admin can also add new pizzas to the database from **"Create New Pizza"** page. Again the recipe and the price for the pizza will be shown in the text box every time admin adds or removes any extension. If the same recipe or ID or Name exists, admin will be prompted with the messagebox indicating that this pizza already exists.
