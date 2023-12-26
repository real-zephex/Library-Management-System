# Library Management System
import os
import sqlite3
import importlib

module_info = {
	"admin":None,
	"user":None
}
user_status = None
enabled_modules = []

# Connect to SQLite database
connection = sqlite3.connect("databases/library.db")

cursor = connection.cursor()

def create_database():
	# This will create a table named books and will ignore if it already exists
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS books (
			ID INTEGER NOT NULL,
			Book TEXT NOT NULL,
			Author TEXT NOT NULL,
			Published_on TEXT NOT NULL,
			Publisher TEXT NOT NULL,
			Copies TEXT
		)
	''')

def import_check():
	'''
		This function will check whether the admin.py and user.py files have any issues or not.
	'''
	for i in module_info.keys():
		try:
			module = importlib.import_module(i)
			module_info[i] = module
		except ImportError as _:
			module_info[i] = False
		except (NameError, SyntaxError) as _:
			module_info[i] = False

	disabled_modules = [i for i in module_info.keys() if module_info[i] == False]
	return disabled_modules

def menu():
	global user_status
	print(
		"""
			Welcome to XYZ Library
		"""
	)
	while user_status not in ["user", "admin"]:
		user_status = input("Are you a user or an admin: ").lower()

	if user_status in import_check():
		print("Apologies but it is not available right now.") 
		exit()
	
	if user_status == "user":
		module_info["user"].User(input("Enter your user id: "))

	elif user_status == "admin":
		pass

os.system("cls")
menu()

connection.commit()
connection.close()