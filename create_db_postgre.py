from psycopg2 import connect, OperationalError
db_name = "imdb"
sql = f"CREATE DATABASE {db_name};"
try:
    cnx = connect(user="postgres", password="password", host="localhost")
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(sql)
    print(f"Database {db_name} has been created.")
except OperationalError:
    print("Error !")
else:
    cursor.close()
    cnx.close()