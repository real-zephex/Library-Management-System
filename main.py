import os
import sqlite3
import admin, user

# Connect to SQLite database
mydb = sqlite3.connect("databases/library.db")

cursor = mydb.cursor()

def create_db():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            ID INTEGER NOT NULL,
            BOOK_NAME VARCHAR(30) NOT NULL,
            AUTHOR_NAME VARCHAR(30) NOT NULL,
            PUBLISHING_DATE DATE,
            NUMBER_OF_COPIES_AVAILABLE INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_books(
            Registration_Number INTEGER NOT NULL,
            Recipient_Name VARCHAR(30) NOT NULL,
            Borrowed_Book_ID INTEGER NOT NULL,
            Borrowed_Book_Name VARCHAR(30) NOT NULL,
            Number_of_Copies_Borrowed INTEGER NOT NULL
        )
    ''')
    
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS user_info(
    #         Registration_Number INTEGER NOT NULL,
    #         Recipient_Name VARCHAR(30) NOT NULL,
    #         Borrowed_Books_IDs INTEGER NOT NULL,
    #         Borrowed_Books_Names VARCHAR(30) NOT NULL,
    #         Number_of_Copies_Borrowed INTEGER NOT NULL
    #     )
    # ''')

    mydb.commit()
    mydb.close()

def menu():
    user_status = None
    print("""
            Welcome to XYZ Library!!!
        """)
    while user_status not in ["admin", "user"]:
        user_status = input("Would you like to access the database as an admin user or a user? : ").lower()
    
    if user_status == "admin":
        admin.authentication()
    elif user_status == "user":
        user.start()

menu()
# create_db()