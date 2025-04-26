from tkinter import*
import mysql.connector as mysql
# from tk import messagebox

win = Tk()
win.geometry("200x200")

lroll = Label(win,text="Roll No")
lroll.grid(row=0,column=0)
eroll = Entry(win)
eroll.grid(row=0,column=1)

lname = Label(win,text="Student name")
lname.grid(row=1,column=0)
ename = Entry(win)
ename.grid(row=1,column=1)

lsem = Label(win,text="Student Sem")
lsem.grid(row=2,column=0)
esem = Entry(win)
esem.grid(row=2,column=1)


def submit():
    roll = eroll.get()
    name = ename.get()
    sem = esem.get()

    connection = mysql.connect(host="localhost",user="root",
                               password="792004",database="python")
    # cursor is return query 
    cursor = connection.cursor()  
    query_str = "INSERT INTO student (roll no , stuname , sem) values (%s, %s, %s)" 
    data = (roll,name,sem)   

    cursor.execute(query_str,data)
    cursor.execute("commit")

    connection.close()

    # messagebox.INFO("insert status","data inserted")

submit = Button(win,text="submit",command=submit)
submit.grid(row=3,column=0)

def delete():
    roll = eroll.get()
    name = ename.get()
    sem = esem.get()

    connection = mysql.connect(host="localhost",user="root",
                               password="hashumati",database="python")
    # cursor is return query 
    cursor = connection.cursor()  
    query_str = "DELETE FROM student where rollno="+roll  

    cursor.execute(query_str)
    cursor.execute("commit")

    connection.close()

delete = Button(win,text="Delete",command=delete)
delete.grid(row=3,column=1)

def update():
    roll = eroll.get()
    name = ename.get()
    sem = esem.get()

    connection = mysql.connect(host="localhost",user="root",
                               password="hashumati",database="python")
    # cursor is return query 
    cursor = connection.cursor()  
    query_str = "UPDATE student  SET  stuname = %s, sem = %s  WHERE rollno="+roll  
    data = (name,sem)

    cursor.execute(query_str,data)
    cursor.execute("commit")

    connection.close()

update = Button(win,text="Update",command=update)
update.grid(row=4,column=0)


def fetch():
    # roll = eroll.get()
    # name = ename.get()
    # sem = esem.get()

    connection = mysql.connect(host="localhost",user="root",
                               password="hashumati",database="python")
    # cursor is return query 
    cursor = connection.cursor()  
       
    cursor.execute("SELECT * FROM student")
    # cursor.execute("SELECT * FROM student where rollno="+roll) # comment out get roll to use this 

    result = cursor.fetchall()

    for i in result:
        print(i[1])

    cursor.execute("commit")

    connection.close()

    # messagebox.INFO("insert status","data inserted")

fetch = Button(win,text="fetch",command=fetch)
fetch.grid(row=4,column=1)

win.mainloop()  