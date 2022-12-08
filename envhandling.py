from dotenv import load_dotenv
import os

load_dotenv()


def create_sql_data(user, password, host, db):
    os.remove(".env")
    f = open(".env", "w")
    with open(".env", "w") as f:
        f.write("SQL_USER=" + user + "\n")
        f.write("SQL_PASSWORD=" + password + "\n")
        f.write("SQL_HOST=" + host + "\n")
        f.write("SQL_DB=" + db + "\n")
def get_sql_data(data):
    if data == "user":
        return os.getenv('SQL_USER')
    if data == "password":
        return os.getenv('SQL_PASSWORD')
    if data == "host":
        return os.getenv('SQL_HOST')
    if data == "db":
        return os.getenv('SQL_DB')
    if data == "all":
        data = (('user', os.getenv('SQL_USER')), ('paswd', os.getenv('SQL_PASSWORD')), ('host', os.getenv('SQL_HOST')), ('db', os.getenv('SQL_DB')))
        return data
    else:
        return "smth went wrong"