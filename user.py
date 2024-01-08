import re
import os
import pandas as pd
import sqlite3
from tabulate import tabulate

mydb = sqlite3.connect("databases/library.db")

cursor = mydb.cursor()

def authentication():
    """
        Somehow find a way to check the username alongside asking the user for the correct username.
    """
    pattern = re.compile(r'^[a-z]+_+[a-z]+@+\d{4}$')
    global username
    username = input("Enter username: ")
    
    while not pattern.match(username):
        print("Incorrect username.")
        username = input("Enter correct username: ")



def menu():
    options = {
        1: "Borrow Books",
        2: "Return Books",
        3: "Display Books",
        4: "Exit"
    }

    print("Choose from the following option: ")
    for i, j in options.items():
        print(f"{i}. {j}")

    user_choice = None
    while user_choice not in options:
        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError as e:
            print("Invalid input")
            menu()
    
    match user_choice:
        case 1:
            borrow_books()
        case 2:
            return_books()
        case 3:
            display_books()
        case 4, _:
            exit()

def borrow_books():
    data = username.split("@")
    print(data)

def return_books():
    pass

def display_books():
    os.system("clear")
    print ("""
                            Info on Table books
    """)
    cursor.execute('''
        select * from books;
    ''')
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns = columns)
    print(tabulate(df, headers = columns, tablefmt='pretty', showindex = 'never'), "\n\n") # type: ignore 

    menu()


def start():
    authentication()
    menu()
