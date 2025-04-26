import mysql.connector as mysql
#pip3 intstall mysql-connector-python


roll=input("Enter the Roll NO")
name=input("Enter the Student name")
sem = input("Enter the Semeter")


#connection
connection = mysql.connect(host="localhost",user="root",password="792004",database="student")
cursor = connection.cursor()

#use placeholder to safely insert data
insert_query = "insert into student(rollno, stuname , semester) values (%s, %s, %s)"

data = (roll,name,sem) 

cursor.execute(insert_query,data)

#cursor
#cursor = connection.cursor()
#cursor.execute("insert into student (rollno , stuname ,semester) values (3,'John',5)")

#commit the changes
connection.commit()
print("Data Inserted Into databse")

#cursor.execute("commit")


#close the connection
connection.close()