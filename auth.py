"""PACKAGES"""

import re
from mysqlhandling import *
from envhandling import *
from cryptography.fernet import Fernet, InvalidToken

def decrypt(password):
	decrypted = ""
	try:
		with open('filekey.key', 'rb') as filekey: 
			key = filekey.read() 
		
		fernet = Fernet(key) 
		decrypted = fernet.decrypt(password) 
  
	except InvalidToken:
		print("Du hast entweder einen ungültigen Schlüssel oder deine Datei ist schon entschlüsselt.")
	
	decrypt = decrypted.decode('utf-8')
	
	return decrypt

def encrypt(password):
	with open('filekey.key', 'rb') as filekey: 
		key = filekey.read()
	fernet = Fernet(key) 
	encrypted = fernet.encrypt(bytes(password, encoding='utf8'))
	return encrypted


def isvalidEmail(email):
    pattern = "^\S+@\S+\.\S+$"
    objs = re.search(pattern, email)
    try:
        if objs.string == email:
            return True
    except:
        return False

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def is_valid(email, username, password1, password2):
	"""VALID VARIABLES"""
	password_match = False
	password_long = False
	password_has_numbers = False
	username_valid = False
	authentication_valid = False
	err_msg = []
	

	"""CHECK IF GIVEN DATA IS VALID"""
	email_valid = isvalidEmail(email)
	if email_valid is False:
		err_msg.append("This Email is not valid")
	
	contains_uppercase = any(char.isupper() for char in password1)

	if password1 == password2:
		password_match = True
	else:
		err_msg.append("Passwords were not the same")

	if len(password1) >= 8:
		password_long = True
	else:
		err_msg.append("The password must be longer than 8 characters")

	if has_numbers(password1) == True:
		password_has_numbers = True
	else:
		err_msg.append("The password must contain numbers")

	if len(username) <= 15:
		username_valid = True
	else:
		err_msg.append("The username cannot be longer than 15 characters")


	if contains_uppercase == True & email_valid == True & password_match == True & password_long == True & password_has_numbers == True & username_valid == True:
		authentication_valid = True
	return authentication_valid, err_msg

def register(email, username, password, password2):
	"""Check if Registration is valid"""
	valid = is_valid(email, username, password, password2)
	if valid[0] == True:
		insert_user_data(username, email, encrypt(password))
		return "Successfull"
	else:
		err_msg = valid[1]
		return err_msg

def login_name_and_passwd(username, password):
	user_data = get_pswd_username(username)
	given_pswd = decrypt(user_data[0][1])
	if given_pswd == password:
		return True
	else:
		return False


