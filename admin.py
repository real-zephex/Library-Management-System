import os
import sqlite3
import pandas as pd
from tabulate import tabulate

connection = sqlite3.connect("databases/library.db")
cursor = connection.cursor()

def authentication():
    username, password = None, None
    while username != "admin" or password != "abc_def":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("============================")
        
    menu()

def menu():
    os.system("clear")

    options = {
        1: "Update Books",
        2: "Add Books",
        3: "Exit"
    }

    print("Choose from the following options:")
    for i, j in options.items():
        print(f"{i}. {j}")

    user_choice = None
    while user_choice not in options:
        try: 
            user_choice = int(input("Enter your choice: "))
        except ValueError as e:
            print("Invalid input.")
            menu()

    match user_choice:
        case 1:
            update_books()
        case 2:
            enter_books()
        case 3, _:
            exit()


def update_books():
    

    admin_preference = None

    print("\n1. Delete Record(s). \n2. Correction. \n3. Update number of available copies. \n4. View Database\n")

    while admin_preference not in [1, 2, 3, 4]:
        admin_preference = int(input("Enter your choice:"))

    if admin_preference == 1:
        id = int(input("Enter the ID for the record you wish to delete: "))
        cursor.execute(f'''
            delete from books where ID = {id};
        ''')

        menu()
        
    elif admin_preference == 2:
        rec = input ("Enter the id you wish to update: ")
        col = input ("Enter the column you wish to update: ")
        upcol = input ("Enter the updated value: ")
        cursor.execute(f'''
            update books set "{col}" = "{upcol}" where ID= {rec};
        ''')

        menu()


    elif admin_preference == 3:

        book_id = int(input("Enter the book id for which you'd like to update the available copies: "))

        cursor.execute(f'''
            select NUMBER_OF_COPIES_AVAILABLE from books where ID = {book_id}
        ''')
        rows = cursor.fetchone()[0]

        print(f"Current number of copies available: {rows} ")
        updated_copies = int(input("Enter updated value for 'number of available copies': "))
        cursor.execute(f'''
            update books set NUMBER_OF_COPIES_AVAILABLE = {updated_copies} where ID = {book_id};
        ''')

        menu()


        print ("""
                              Info on Table books
        """)
        cursor.execute('''
            select * from books;
        ''')
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns = columns)
        print(tabulate(df, headers = columns, tablefmt='pretty', showindex = 'never')) # type: ignore 

        menu()


def enter_books():
    
    cursor.execute('''
        select ID from books;
    ''')
    rows = cursor.fetchall()
    x = rows[len(rows) - 1][0]

    book_name=input("Enter Book name: ")
    author_name = input("Enter author name: ")
    pub_date = int(input("Enter publishing date in the format yyyymmdd: "))
    copies = int(input("Enter number of copies available: "))

    cursor.execute(f'''
        insert into books (ID, BOOK_NAME, AUTHOR_NAME, PUBLISHING_DATE, NUMBER_OF_COPIES_AVAILABLE) values 
        ({x+1},"{book_name}","{author_name}",{pub_date},{copies});
    ''')

    menu()


authentication()

connection.commit()
connection.close()