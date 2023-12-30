import sqlite3
import pandas as pd
from tabulate import tabulate

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
    update_books()

def update_books():
    

    admin_preference = None
    """
        This function will provide the admin with multiple features to maintain the records.
        Admin can choose to:
            1. Delete Records.
            2. Make Corrections.
            3. Update the stock.
            4. View Database.
    """

    print("\n1. Delete Record(s). \n2. Correction. \n3. Update number of available copies. \n4. View Database\n")

    while admin_preference not in [1, 2, 3, 4]:
        admin_preference = int(input("Enter your choice:"))

    # Delete Records
    if admin_preference == 1:
        id = int(input("Enter the ID for the record you wish to delete: "))
        cursor.execute(f'''
            delete from books where ID = {id};
        ''')
        
    # Correction    
    elif admin_preference == 2:
        col = input ("Enter the column you wish to update: ")
        upcol = input ("Enter the updated value: ")
        cursor.execute('''
            update books set col = upcol;
        ''')

    # Update number of books
    elif admin_preference == 3:
        id = input("Enter the book id for which you'd like to update the available copies")
        n = int(input("Enter updated value for 'number of available copies': "))
        cursor.execute(f'''
            update books set NUMBER_OF_COPIES_AVAILABLE = n where ID = {id} ;
        ''')
    
    # View Database - DONE
    elif admin_preference == 4:
        print ("""
                              Info on Table books
        """)
        cursor.execute('''
            select * from books;
        ''')
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns = columns)
        print(tabulate(df, headers = columns, tablefmt='pretty', showindex = 'never'))

update_books()

def enter_books():
    cursor.execute('''
        Insert into books values 
        (111,"The Great Gatsby","F.Scott Fitzgerald", 19250410, 100);
    ''')

# enter_books()

connection.commit()
connection.close()