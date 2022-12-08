from auth import *
from getpass import getpass

def try_login():
    username = input("Username: ")
    password = getpass()
    if login_name_and_passwd(username, password) == True:
        print("Login successfull as " + username)
    if login_name_and_passwd(username, password) == False:
        print("Something went wrong!")
        try_again = input("Try again or Register? --> T or R")
        if try_again == "T":
            try_login()
        if try_again == "R":
            try_register()


    
        



def try_register():
    username = input("Username: ")
    email = input("E-Mail: ")
    password = getpass()
    password2 = getpass()
    if register(str(email), str(username), str(password), str(password2)) == "Successfull":
        print("You are successfully registerd!")
    else:
        err_msg = register(email, username, password, password2)
        i = 0
        while i < len(err_msg):
            print(str(i + 1) + ". " + err_msg[i])
            i = i+1
        try_again = input("Try again or Cancel? --> T or C")
        if try_again == "T":
            try_register()
        if try_again == "C":
            print("Ok!")





in_or_up = input("Login or Register --> type: L or R")

if in_or_up == "L":
    try_login()
if in_or_up == "R":
    try_register()
    