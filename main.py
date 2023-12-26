import os
import sqlite3
import admin, user

# Connect to SQLite database
mydb = sqlite3.connect("databases/library.db")

cursor = mydb.cursor()

def create_db():
    # This will create a table named "books" and if already exists, then ignore.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            ID INTEGER NOT NULL,
            BOOK_NAME VARCHAR(30) NOT NULL,
            AUTHOR_NAME VARCHAR(30) NOT NULL,
            PUBLISHING_DATE DATE,
            NUMBER_OF_COPIES_AVAILABLE INTEGER
        )
    ''')
    
    # This will create a table named "borrowed_books" and if already exists, then ignore.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_books(
            Recipient_Name VARCHAR(30) NOT NULL,
            Borrowed_Books VARCHAR(30) NOT NULL,
            Days_Left NOT NULL
        )
    ''')
    
    mydb.commit()
    mydb.close()

user_status = None
def main():
    global user_status
    print("""
            Welcome to XYZ Library!!!
        """)
    while user_status not in ["admin", "user"]:
        user_status = input("Would you like to access the database as an admin user or a user? : ").lower()
    
    if user_status == "admin":
        print("Yay")
    elif user_status == "user":
        print("Woohooo!")

# os.system("cls")
main()
# create_db()