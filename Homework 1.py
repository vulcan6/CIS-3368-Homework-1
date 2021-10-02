# Homework 1
# Erick Jimenez
# 1463639
# Hey Professor! I've been uploading to my own personal GitHub. I skimmed through the details of the homework and missed this part. *sad*

from re import U
import mysql.connector
from mysql.connector import Error
import datetime
from datetime import datetime

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
    [d] Delete Item
    [u] Update item details
    [r1] Output all items in alphabetical order
    [r2] Output all items by sorted quantity
    [q] Quit Session """)

menu()
option = str(input("Enter your option: "))

# simple UI no actual established working keys yet

while option != "q":
    #sorting options
    if option == "a":
        #add item action
        item_from_user =  str(input("What item would you like to add?  "))
        item_amount = int(input("How much would you like to add?  "))
        now=datetime.now()
        item_dateadded = now.strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO shoppinglist (itemdescription, quantity, dateadded) VALUES ('%s', %s, '%s')" % (item_from_user, item_amount, item_dateadded)

        execute_query(conn, query)

    elif option == "d":
        # delete action
        for shoppinglist in rows:
            print(shoppinglist)
        print("What item would you like to delete?  ")
        item_to_delete = int(input())
        delete_statement = "DELETE FROM shoppinglist WHERE id = %s" % (item_to_delete)

        execute_query(conn, delete_statement)
        # Does delete ID but does not update immediately. Need to quit and run code again for updated shopping list.

    elif option == "u":
        # update action
        for shoppinglist in rows:
            print(shoppinglist)
        idnum = int(input("What item would you like to update?  "))
        quantitynum = int(input("New Amount:  "))
        update_invoice_query = """
        UPDATE shoppinglist
        SET quantity = %s
        WHERE id = %s """ % (quantitynum, idnum)
# Established a working update query
        execute_query(conn, update_invoice_query)

        
    elif option == "r1":
        # alphabetical order
        for shoppinglist in rows:
            print(shoppinglist)
    elif option == "r2":
        # sorted quantity
        print()
    else:
        print("Read the damn menu.")
    #got quit to work Tada
    menu()
    option = str(input("Enter your option: "))

print("Goodbye User!")

    

