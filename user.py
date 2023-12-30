import re

def authenticate(username):
    pattern = re.compile(r'^[a-zA-Z]+_[a-zA-Z]+@\d{4}$')
    if pattern.match(username):
        print("Username matched")
    else:
        print("Username no no get lost")

authenticate("sumit_kumar@000")