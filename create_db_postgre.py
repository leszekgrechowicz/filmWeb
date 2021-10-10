from psycopg2 import connect, OperationalError

db_name = "imdb"
sql = f"CREATE DATABASE {db_name};"

db_created = False

db_choice = input("\nWelcome in film_Web DataBase creator !\n"
                  "\nPlease confirm what Data Base is installed on your machine.\n"
                  "Please choice from the following: \n\n"
                  "\t1 - PostgreSQL\n"
                  "\t2 - SQLite\n"
                  "\t2 - MySQL\n"
                  "\n>>> ")

while not db_created:

    user = input("Please provide Data-Base user name: ")
    password = input("Password: ")

    try:
        cnx = connect(user=f"{user}", password=f"{password}", host="localhost")
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql)
        print(f"Database {db_name} has been created.")
        db_created = True


    except OperationalError as error:
        print(f"Error ! --> {error} ")
    else:
        cursor.close()
        cnx.close()
