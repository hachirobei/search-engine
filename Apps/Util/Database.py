import pymysql

HOST = "localhost"
USER = "your_mysql_username"
PASSWORD = "your_mysql_password"
DATABASE = "your_database_name"

def get_connection():
    """Return a new connection to the database."""
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )