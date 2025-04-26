import mysql.connector as mysql

# conection
connection = mysql.connect(host="localhost",user="root",
                           password="792004",database="student")

rollno = 4
stuname = max
sem = 3

connection.close()