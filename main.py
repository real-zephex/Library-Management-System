# Library Management System
import sqlite3

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



connection.commit()
connection.close()