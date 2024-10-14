import mysql.connector

DB = mysql.connector.connect(user='root', password='qwerty@123',
                              host='127.0.0.1',
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