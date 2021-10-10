from psycopg2 import connect, OperationalError
import re

db_name = "imdb"

db_choice = input("\nWelcome in film_Web DataBase creator !\n"
                  "\n>>> ")

connected = False
while not connected:

    user = input("Please provide Data-Base user name: ")
    password = input("Password: ")

    try:
        cnx = connect(user=f"{user}", password=f"{password}", host="localhost")
        cnx.autocommit = True
        connected = True

    except OperationalError as error:
        print(f"Error ! --> {error} ")


db_created = False
while not db_created:

    print("You are successfully connected to the database")

    sql = f"CREATE DATABASE {db_name};"

    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        print(f"Database {db_name} has been created.")
        db_created = True

    except OperationalError as error:
        print(f"Error ! --> {error} ")
    else:
        cursor.close()
        cnx.close()
