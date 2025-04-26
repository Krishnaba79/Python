import mysql.connector as mysql
# pip3 install mysql-connector-python

roll= input("Enter Your Roll No : ")
name= input("Enter Studentname : ")
sem= input("Enter Your Sem : ")

connection = mysql.connect(host="localhost",user="root",
                           password="792004",database="python")
cursor = connection.cursor()

# use placeholder to sefely insert data
insert_query = "INSERT INTO student (rollno , stuname, sem) VALUES (%s, %s, %s)"

data = (roll , name , sem)
cursor.execute(insert_query,data)

# commit the changes
connection.commit()
print("Data Inserted Into Database")

# close the connection
connection.close()