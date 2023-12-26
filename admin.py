import sqlite3

# Connecting to the database and all
connection = sqlite3.connect("databases/library.db")
cursor = connection.cursor()

def authentication():
    username, password = None, None
    # This will verify whether the user is actually an admin user or not.
    while username != "admin" or password != "abc_def":
        # Above taken are examples only. You are advised to use strong credentials.
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("============================")
    return True

def update_books():
    print("1. Delete record(s).")
    print("2. Correction")
    print("3. ")
    
    f=

authentication()
