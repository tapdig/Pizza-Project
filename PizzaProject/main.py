from tkinter import *
from PIL import Image, ImageTk
from database import Database
from MainPart import Main

def main():
	db = Database()
	root = Tk()
	root.title("LOGIN FORM")
	root.geometry("686x1220")
	bg_image = PhotoImage(file = r"Photos/pizza_logo.png")
	Label(root, image = bg_image).place(relwidth = 1, relheight = 1)
	Main(root)
	root.mainloop()

if __name__ == "__main__":
	main()
	