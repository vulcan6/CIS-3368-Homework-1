# Homework 1
# Erick Jimenez
# 1463639

import mysql.connector
from mysql.connector import Error
import datetime
from datetime import date

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

conn = create_connection("cis3368.cdmtjsnscdxt.us-east-2.rds.amazonaws.com", "admin", "Infernus0!", "cis3368")
cursor = conn.cursor(dictionary=True)
sql = "SELECT * FROM shoppinglist"
cursor.execute(sql)
rows = cursor.fetchall()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Just realized the ease of just importing from the sql file and making this portion less clunky. Noted for future assignments. 

#Beginning creation of menu.
def menu():
    print("""
    Welcome User!
    What would like to do with the database?
    [a] Add Item
    [d] Remove Item
    [u] Update item details
    [r1] Output all items in alphabetical order
    [r2] Output all items by sorted quantity
    [q] Quit Session """)

menu()
option = str(input("Enter your option: "))

# simple UI no actual established working keys yet

