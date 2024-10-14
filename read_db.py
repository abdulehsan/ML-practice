import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
dbUser = os.getenv('db_user')
dbPwd = os.getenv('db_pwd')
dbHost = os.getenv('db_host')

DB = mysql.connector.connect(user=dbUser, password=dbPwd,
                              host=dbHost,
                              database='sakila')

if DB.is_connected():
    print("Succesfully connected!")

    cursor = DB.cursor()

    query = "SELECT city.city, country.country\
            FROM city\
            JOIN country ON city.country_id = country.country_id\
            ORDER BY country.country ASC;"

    cursor.execute(query)

    result = cursor.fetchall()

    for rows in result:
        print(rows)

else:
    print("Not Connected!")
DB.close()