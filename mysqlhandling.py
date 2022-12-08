"""Connect to MySQL DB"""
import mysql.connector
from envhandling import * 


cnx = mysql.connector.connect(user=get_sql_data("user"), password=get_sql_data("password"),
                              host=get_sql_data("host"),
                              database=get_sql_data("db"))
curr = cnx.cursor()

def create_user_data_tabel():
    curr.execute("CREATE TABLE user_data (id int PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255), perms VARCHAR(255) DEFAULt 'default')")

def insert_user_data(username, email, password):
    sql = "INSERT INTO user_data (username, email, password, perms) VALUES (%s, %s, %s, %s)"
    val = (username, email, password, "default")
    curr.execute(sql, val)
    cnx.commit()
    print(curr.rowcount, "record inserted.")
def get_pswd_username( username):
    sql = "SELECT username, password FROM user_data WHERE username = %s"
    val = (username, )
    curr.execute(sql, val)
    return curr.fetchall()