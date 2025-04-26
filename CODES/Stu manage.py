from tkinter import*
from tkinter import messagebox

class Student:
        def __init__(self,name,email,Sem):
                self.StudentName = name
                self.StudentEmail = email
                self.StudentSem = Sem 

StudentList =[]
                
win = Tk()
win.title("STUDENT MANAGEMENT")
win.geometry("1500x800")

# w=win.winfo_screenwidth
# h=win.winfo_screenheight
# win.geometry("{}x{}".format(w,h))

heading = Label(win,text="STUDENT MANAGEMENT",font="Arial 24 bold")
heading.place(x=500,y=30)

name = Label(win,text="Student Name :",font="Arial 16 bold")
name.place(x=10,y=100)
nentry = Entry(win,width=30)
nentry.place(x=175,y=105)

rollno = Label(win,text="Student Roll No :",font="Arial 16 bold")
rollno.place(x=10,y=150)
rentry = Entry(win,width=30)
rentry.place(x=190,y=155)

email = Label(win,text="Student Email :",font="Arial 16 bold")
email.place(x=400,y=100)
ementry = Entry(win,width=40)
ementry.place(x=575,y=105)

sem = Label(win,text="Student Sem :",font="Arial 16 bold")
sem.place(x=900,y=100)
sentry = Entry(win,width=20)
sentry.place(x=1055,y=105)

Details = Label(win,text="Student Details :",font="Arial 16 bold")
Details.place(x=200,y=200)

tableLabel = Label(win,text="None",font="Arial 24 bold")
tableLabel.place(x=100,y=300)

def addbtn():
        stuName = nentry.get()
        stuEmail = ementry.get()
        stuSem = sentry.get()

        s1 = Student(stuName,stuEmail,stuSem)
        StudentList.append(s1)

        nentry.delete(0,END)
        ementry.delete(0,END)
        sentry.delete(0,END)

addbtn = Button(win,text="Add Student",command=addbtn,bg="white",font="Arial 16 bold")
addbtn.place(x=1250,y=90)

updateRollNo = 0

def updatebtn():
        stuName = nentry.get()
        stuEmail = ementry.get()
        stuSem = sentry.get()

        # update
        StudentList[updateRollNo].StudentName = stuName
        StudentList[updateRollNo].StudentEmail = stuEmail
        StudentList[updateRollNo].StudentSem = stuSem


        nentry.delete(0,END)
        ementry.delete(0,END)
        sentry.delete(0,END)

        showstu()

updatebtn = Button(win,text="Update Student",command=updatebtn,bg="white",font="Arial 16 bold")
updatebtn.place(x=1250,y=150)

def showstu():
        table = "Roll no \t \t Student Name \t \t Student Email \t \t Student Semester"

        rollNo = 1

        for stu in StudentList:
                table +="\n{} \t\t\t {} \t\t\t {} \t\t\t {}".format(rollNo,stu.StudentName,stu.StudentEmail,stu.StudentSem)
                rollNo += 1

        tableLabel.config(text=table)


showbtn = Button(win,text="Show",command=showstu,bg="white",font="Arial 16 bold")
showbtn.place(x=400,y=200)


def deletebtn():
        print("Delete the btn was clicked")
        roll = int(rentry.get())
        index = roll-1
        StudentList.pop(index)
        showstu()
        rentry.delete(0,END)

deletebtn = Button(win,text="delete Student",command=deletebtn,bg="white",font="Arial 16 bold")
deletebtn.place(x=500,y=150)



def getbtn():
        roll = int(rentry.get())
        index = roll-1

        global updateRollNo
        updateRollNo = index
        

        if(index < len(StudentList)):   
                nentry.delete(0,END)
                ementry.delete(0,END)
                sentry.delete(0,END)


                nentry.insert(0,StudentList[index].StudentName)
                ementry.insert(0,StudentList[index].StudentEmail)
                sentry.insert(0,StudentList[index].StudentSem)

        else:
                messagebox.showerror("ERROR","Invalid roll no")
                
getbtn = Button(win,text="get Student",command=getbtn,bg="white",font="Arial 16 bold")
getbtn.place(x=360,y=150)

win.mainloop()